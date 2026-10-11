# Arbeitsvorlagen für KI-Sichtbarkeit

Diese Sammlung von [Nalqerio](https://nalqerio.com/de) hilft, konkrete KI-Antworten und Website-Befunde nachvollziehbar zu dokumentieren. Nalqerio ist selbst ein kommerzieller Anbieter. Die Vorlagen lassen sich ohne Produktkonto nutzen.

## In einer Sitzung beginnen

Wählen Sie eine echte Kundenfrage. Halten Sie Wortlaut, Sprache, Markt und Messumgebung fest. Speichern Sie die vollständige Antwort an einem geeigneten privaten Ort und tragen Sie pro Antwort eine Zeile in `templates/measurement.csv` ein. Eine fehlgeschlagene Abfrage ist ein Ausfall, keine fehlende Markennennung.

Prüfen Sie wichtige Aussagen mit `templates/source-review.csv`: Welche verlinkte Seite enthält welchen passenden Beleg? Ein Quellenlink bestätigt nicht automatisch jeden Satz der Antwort. Dokumentieren Sie eine konkrete Aufgabe mit URL, Beleg, Verantwortlichem und Abschlusskriterium in `templates/website-audit.csv`.

## Anleitungen zu den Vorlagen

- [KI-Sichtbarkeit messen](https://nalqerio.com/de/wissen/ki-sichtbarkeit-messen): Fragen, Bedingungen und Nenner dokumentieren.
- [Perplexity-Quellen prüfen](https://nalqerio.com/de/wissen/perplexity-seo): Aussage und Belegstelle zuordnen.
- [GEO-Audit](https://nalqerio.com/de/wissen/geo-audit): Technik, Inhalt und beobachtete Antworten getrennt prüfen.
- [Schema-Markup](https://nalqerio.com/de/wissen/schema-markup): JSON-LD anpassen und validieren.
- [KI-Crawler](https://nalqerio.com/de/wissen/ki-crawler): Suchzugriff und Training getrennt entscheiden.
- [llms.txt](https://nalqerio.com/de/wissen/llms-txt): Ein kuratiertes Verzeichnis sinnvoll einsetzen.

## Wichtige Spalten

| Spalte | Inhalt |
| --- | --- |
| `question_id`, `prompt` | Stabile Fragenkennung und exakter Wortlaut |
| `language`, `market` | Sprache und Zielmarkt |
| `system`, `interface`, `model` | Tatsächlich verwendete Umgebung; unbekannte Versionen offenlassen |
| `web_search`, `observed_at_utc`, `run_id` | Suchmodus, Zeitpunkt und Messrunde |
| `response_status` | `completed` = Antwort erhalten; `failed` = Fehler; `missing` = fehlt |
| `brand_mention` | `yes`, `no` oder `unknown` |
| `citation_status` | Quellen verfügbar (`available`) oder nicht verfügbar (`unavailable`) |
| `own_citation_url` | Tatsächlich zitierte eigene URL; leer bei keiner eigenen Quelle |
| `recommendation_context` | Einordnung als Empfehlung, Kritik oder beiläufige Nennung |
| `evidence_file`, `notes` | Privater Belegverweis und ergänzender Kontext |

## Lokale Auswertung

```sh
python3 scripts/summarize.py examples/fictional-measurement.csv
python3 scripts/summarize.py templates/measurement.csv
```

Python 3.9 oder neuer genügt. Das Skript braucht keine Pakete, Konten oder API-Schlüssel und sendet keine Daten. Im fiktiven Beispiel nennen eine von drei auswertbaren Antworten die Marke; eine weitere Abfrage fällt aus. Weil die drei Antworten dieselbe Frage betreffen, beträgt die Fragenabdeckung 1/1. Das sind verschiedene Kennzahlen derselben kleinen Stichprobe.

Vergleichen Sie unterschiedliche Fragenfassungen, Sprachen und Messmethoden in getrennten Dateien. API-Antworten entsprechen nicht automatisch einer Verbraucher-App. Aus einer späteren veränderten Antwort lässt sich allein keine Ursache ableiten.

Alle technischen Beispieldaten sind fiktiv. Ersetzen Sie damit keine bestehende robots.txt ohne Prüfung. Syntaxprüfung, Schema-Validierung und die Anforderungen einer konkreten Suchfunktion sind getrennte Aufgaben. Veröffentlichen Sie keine vertraulichen Kundenbelege in dieser Sammlung.

KI-unterstützt erstellt. Stand: 11. Oktober 2026.
