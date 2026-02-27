"use client";

import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";

export default function AjustesPage() {
  return (
    <AppShell>
      <TopBar title="Ajustes" subtitle="Plan, exportacion, privacidad" />
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-xl font-display mb-3">Plan actual</h3>
          <p>Core - 9,99 EUR/mes</p>
          <div className="mt-3 space-y-2">
            <button className="px-3 py-2 rounded-xl bg-black text-white w-full">
              Upgrade a Peace of mind
            </button>
            <button className="px-3 py-2 rounded-xl border w-full">
              Ver facturas
            </button>
          </div>
        </div>
        <div className="card">
          <h3 className="text-xl font-display mb-3">Privacidad y datos</h3>
          <div className="space-y-2 text-sm">
            <div>Retencion: 12 meses</div>
            <div>Exportacion: JSON + CSV</div>
            <button className="px-3 py-2 rounded-xl border w-full">
              Exportar mis datos
            </button>
          </div>
        </div>
      </div>
    </AppShell>
  );
}
