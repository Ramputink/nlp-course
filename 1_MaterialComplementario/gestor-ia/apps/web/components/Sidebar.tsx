import Link from "next/link";

const nav = [
  { href: "/onboarding", label: "Onboarding" },
  { href: "/dashboard", label: "Bandeja" },
  { href: "/whatsapp", label: "WhatsApp" },
  { href: "/gastos", label: "Gastos" },
  { href: "/ingresos", label: "Ingresos/Facturas" },
  { href: "/checklist", label: "Checklist" },
  { href: "/rag", label: "Pregunta a Gestor.ia" },
  { href: "/notificaciones", label: "Notificaciones" },
  { href: "/partners", label: "Partners" },
  { href: "/ajustes", label: "Ajustes" },
];

export function Sidebar() {
  return (
    <aside className="p-6 bg-[#fff1dd] border-r border-black/10">
      <div className="text-2xl font-bold font-display">Gestor.ia</div>
      <p className="text-sm text-black/70 mt-1">Autonomo Copilot</p>
      <nav className="mt-8 space-y-3">
        {nav.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="block text-[15px] px-3 py-2 rounded-xl hover:bg-black/5"
          >
            {item.label}
          </Link>
        ))}
      </nav>
      <div className="mt-10 p-3 rounded-xl bg-black text-white text-sm">
        Plan Core - 9,99/mes
      </div>
    </aside>
  );
}
