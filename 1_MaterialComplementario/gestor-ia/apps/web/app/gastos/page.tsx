"use client";

import { useEffect, useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";
import { getExpenses } from "@/lib/api";

export default function GastosPage() {
  const [expenses, setExpenses] = useState<any[]>([]);
  const userId = 1;

  useEffect(() => {
    getExpenses(userId).then(setExpenses);
  }, []);

  return (
    <AppShell>
      <TopBar title="Gastos" subtitle="Lista + detalle + origen" />
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 card">
          <h3 className="text-xl font-display mb-3">Listado</h3>
          <div className="space-y-3">
            {expenses.map((exp) => (
              <div key={exp.id} className="p-3 border rounded-xl bg-white">
                <div className="flex justify-between">
                  <div>
                    <div className="font-semibold">{exp.vendor}</div>
                    <div className="text-sm text-black/60">{exp.date}</div>
                  </div>
                  <div className="text-right">
                    <div className="font-semibold">{exp.total} EUR</div>
                    <div className="text-sm text-black/60">{exp.category}</div>
                  </div>
                </div>
                <div className="text-xs text-black/50 mt-2">
                  Confianza: {(exp.confidence ?? 0).toFixed(2)} | Doc: {exp.source_document_id ?? "n/a"}
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className="card">
          <h3 className="text-xl font-display mb-2">Sugerencia deducibilidad</h3>
          <p className="text-sm text-black/70">
            Si el gasto esta vinculado a la actividad, puede ser deducible.
          </p>
          <div className="mt-3 p-3 bg-white border rounded-xl">
            <div className="text-xs uppercase text-black/60">Cita</div>
            <div className="text-sm">
              Source AEAT #1: Gastos necesarios con justificante.
            </div>
            <button className="mt-3 px-3 py-2 rounded-xl border w-full">
              Ver fuente
            </button>
          </div>
        </div>
      </div>
    </AppShell>
  );
}
