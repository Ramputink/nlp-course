"use client";

import { useEffect, useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";
import { StatCard } from "@/components/StatCard";
import { getAlerts, getExpenses, getWhatsappEvents } from "@/lib/api";

export default function DashboardPage() {
  const [expenses, setExpenses] = useState<any[]>([]);
  const [alerts, setAlerts] = useState<any[]>([]);
  const [events, setEvents] = useState<any[]>([]);
  const userId = 1;

  useEffect(() => {
    getExpenses(userId).then(setExpenses);
    getAlerts(userId).then(setAlerts);
    getWhatsappEvents(userId).then(setEvents);
  }, []);

  return (
    <AppShell>
      <TopBar title="Bandeja" subtitle="Resumen operativo y mensajes recientes" />
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <StatCard title="Gastos mes" value={`${expenses.length} items`} footnote="Mock data" />
        <StatCard title="Alertas" value={`${alerts.length}`} footnote="BOE + DEHU" />
        <StatCard title="WhatsApp" value={`${events.length} mensajes`} footnote="Simulado" />
      </div>

      <div className="mt-8 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-xl font-display mb-3">Ultimos mensajes WhatsApp</h3>
          <div className="space-y-3">
            {events.slice(0, 5).map((event) => (
              <div key={event.id} className="p-3 border rounded-xl bg-white">
                <div className="text-sm text-black/60">{event.type}</div>
                <div>{event.payload_json?.text || "Adjunto"}</div>
              </div>
            ))}
          </div>
        </div>

        <div className="card">
          <h3 className="text-xl font-display mb-3">CTA rapido</h3>
          <p className="text-black/70">
            Sube un recibo o envia un audio desde el simulador WhatsApp.
          </p>
          <div className="mt-4 flex gap-3">
            <a className="px-4 py-2 rounded-xl bg-black text-white" href="/whatsapp">
              Ir a WhatsApp
            </a>
            <a className="px-4 py-2 rounded-xl border" href="/gastos">
              Ver gastos
            </a>
          </div>
        </div>
      </div>
    </AppShell>
  );
}
