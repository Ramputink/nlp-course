"use client";

import { useEffect, useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";
import { getAlerts } from "@/lib/api";

export default function NotificacionesPage() {
  const [alerts, setAlerts] = useState<any[]>([]);
  const userId = 1;

  useEffect(() => {
    getAlerts(userId).then(setAlerts);
  }, []);

  return (
    <AppShell>
      <TopBar title="Notificaciones" subtitle="DEHU + BOE + recordatorios" />
      <div className="card space-y-3">
        {alerts.map((alert) => (
          <div key={alert.id} className="p-3 rounded-xl border bg-white">
            <div className="flex justify-between">
              <div>
                <div className="font-semibold">{alert.title}</div>
                <div className="text-sm text-black/60">{alert.body}</div>
              </div>
              <span className="tag">{alert.severity}</span>
            </div>
            <div className="mt-2 text-sm text-black/60">
              Borrador respuesta: Gracias por la notificacion, adjuntaremos docs.
            </div>
            <button className="mt-2 text-sm underline">Enviar (mock)</button>
          </div>
        ))}
      </div>
    </AppShell>
  );
}
