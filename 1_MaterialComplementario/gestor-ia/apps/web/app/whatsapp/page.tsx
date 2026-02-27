"use client";

import { useEffect, useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";
import { ChatBubble } from "@/components/ChatBubble";
import { getWhatsappEvents, sendWhatsappMessage } from "@/lib/api";

export default function WhatsappPage() {
  const [events, setEvents] = useState<any[]>([]);
  const [text, setText] = useState("");
  const userId = 1;

  const refresh = () => getWhatsappEvents(userId).then(setEvents);

  useEffect(() => {
    refresh();
  }, []);

  return (
    <AppShell>
      <TopBar title="WhatsApp simulator" subtitle="Webhook emulator + chat local" />
      <div className="card h-[520px] flex flex-col">
        <div className="flex-1 space-y-3 overflow-auto">
          {events.map((event) => (
            <ChatBubble
              key={event.id}
              role="user"
              text={event.payload_json?.text || "Adjunto"}
            />
          ))}
          <ChatBubble role="system" text="Gestion.ia: Necesito una foto del recibo para completar la extraccion." />
        </div>
        <div className="mt-4 flex gap-3">
          <input
            className="flex-1 px-3 py-2 border rounded-xl"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Escribe un gasto..."
          />
          <button
            className="px-4 py-2 rounded-xl bg-black text-white"
            onClick={async () => {
              if (!text) return;
              await sendWhatsappMessage(userId, text);
              setText("");
              refresh();
            }}
          >
            Enviar
          </button>
        </div>
      </div>
    </AppShell>
  );
}
