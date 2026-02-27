"use client";

import { useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";
import { askRag, getSource } from "@/lib/api";

export default function RagPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState<any>(null);
  const [source, setSource] = useState<any>(null);
  const userId = 1;

  return (
    <AppShell>
      <TopBar title="Pregunta a Gestor.ia" subtitle="RAG gov-only con citas" />
      <div className="card">
        <div className="flex gap-3">
          <input
            className="flex-1 px-3 py-2 border rounded-xl"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ej: puedo deducir gasolina?"
          />
          <button
            className="px-4 py-2 rounded-xl bg-black text-white"
            onClick={async () => {
              const data = await askRag(userId, question);
              setAnswer(data);
              setSource(null);
            }}
          >
            Preguntar
          </button>
        </div>

        {answer && (
          <div className="mt-6 space-y-4">
            <div>
              <div className="text-sm text-black/60">Respuesta</div>
              <div className="text-lg">{answer.answer_text}</div>
              <div className="text-sm text-black/60 mt-2">
                Confianza: {(answer.confidence || 0).toFixed(2)} |{" "}
                {answer.safety?.message}
              </div>
            </div>
            <div className="space-y-3">
              {answer.citations?.map((cite: any) => (
                <div key={cite.source_id} className="p-3 border rounded-xl bg-white">
                  <div className="text-xs uppercase text-black/60">
                    Source {cite.source_id}
                  </div>
                  <div className="text-sm">{cite.snippet}</div>
                  <div className="text-xs text-black/60 mt-1">
                    as_of: {cite.as_of_date}
                  </div>
                  <button
                    className="mt-2 text-sm underline"
                    onClick={async () => {
                      const data = await getSource(cite.source_id, question);
                      setSource(data);
                    }}
                  >
                    Ver fuente
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {source && (
        <div className="card mt-6">
          <h3 className="text-xl font-display">Fuente: {source.title}</h3>
          <p className="text-sm text-black/60">{source.url}</p>
          <div className="mt-3 p-3 bg-white border rounded-xl whitespace-pre-wrap">
            {source.highlighted}
          </div>
        </div>
      )}
    </AppShell>
  );
}
