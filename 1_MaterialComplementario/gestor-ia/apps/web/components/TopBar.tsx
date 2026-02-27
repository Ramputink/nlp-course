export function TopBar({ title, subtitle }: { title: string; subtitle?: string }) {
  return (
    <div className="flex items-center justify-between mb-6">
      <div>
        <h1 className="text-3xl font-display font-semibold">{title}</h1>
        {subtitle && <p className="text-black/60">{subtitle}</p>}
      </div>
      <div className="flex items-center gap-3">
        <span className="tag">Zero-admin</span>
        <div className="text-sm">
          <div className="font-semibold">Ana Lopez</div>
          <div className="text-black/60">ana@autonomos.es</div>
        </div>
      </div>
    </div>
  );
}
