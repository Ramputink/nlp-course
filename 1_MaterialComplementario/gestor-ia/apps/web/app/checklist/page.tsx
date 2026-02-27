"use client";

import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";

const tasks = [
  { id: 1, label: "Modelo 303 (IVA)", due: "2026-01-20", status: "pending" },
  { id: 2, label: "Modelo 130 (IRPF)", due: "2026-01-20", status: "pending" },
  { id: 3, label: "Retenciones 111", due: "2026-01-20", status: "optional" },
];

export default function ChecklistPage() {
  return (
    <AppShell>
      <TopBar title="Checklist Trimestral" subtitle="Q4 2025 (placeholders)" />
      <div className="card">
        <div className="space-y-3">
          {tasks.map((task) => (
            <div key={task.id} className="p-3 rounded-xl border bg-white">
              <div className="flex justify-between">
                <div>
                  <div className="font-semibold">{task.label}</div>
                  <div className="text-sm text-black/60">Vence: {task.due}</div>
                </div>
                <span className="tag">{task.status}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </AppShell>
  );
}
