export type Locale = "es-ES" | "es-MX";

export const messages: Record<Locale, Record<string, string>> = {
  "es-ES": {
    welcome: "Bienvenido a Gestor.ia",
  },
  "es-MX": {
    welcome: "Bienvenido a Gestor.ia",
  },
};

export function t(locale: Locale, key: string) {
  return messages[locale][key] || key;
}
