# vibe-skills - рабочее ядро для ИИ-агентов

> Дали эту ссылку агенту со словами «настройся»? Агент должен прочитать [AGENT-SETUP.md](AGENT-SETUP.md) и выполнить инструкцию.

Самодостаточный комплект из 21 скилла для Claude Code, Codex и совместимых агентов. Внутри также есть навигатор и переносимый протокол работы: Шаг 0, PDCA, проверка результата, уровни инициативы и HANDOFF.

## Состав комплекта

| Блок | Скиллы |
|---|---|
| Рабочий процесс | `using-superpowers`, `brainstorming`, `verification-before-completion` |
| Архитектура и безопасность агента | `agent-harness-construction`, `loop-design-check`, `safety-guard` |
| Интервью и передача работы | `grilling`, `handoff`, `teach`, `wizard`, `to-questionnaire` |
| Аналитика и решения | `data-analyst`, `meeting-insights`, `strategic-advisor` |
| Контент | `content-engine`, `brand-voice` |
| Дизайн и презентации | `slide-craft`, `impeccable`, `ui-ux-pro-max`, `emil-design-eng`, `review-animations` |

Точный маршрутизатор по задачам находится в [`skills/_INDEX.md`](skills/_INDEX.md).

## Быстрый старт

```bash
git clone https://github.com/Yzyvan/vibe-skills.git
```

Для Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -r vibe-skills/skills/* ~/.claude/skills/
```

Для Codex:

```bash
mkdir -p ~/.codex/skills
cp -r vibe-skills/skills/* ~/.codex/skills/
```

Если скиллы уже стоят, не перезаписывайте их вслепую. Попросите агента сравнить версии и показать изменения.

После установки используйте [`AGENTS.template.md`](AGENTS.template.md) как основу для глобального или проектного файла правил. Существующий `CLAUDE.md` или `AGENTS.md` нужно дополнять только после просмотра и подтверждения владельца.

## Что не лежит внутри

Офисные скиллы `docx`, `xlsx`, `pptx` и `pdf` не копируются сюда, потому что их лицензия запрещает распространение. Агент может установить их из официального источника отдельно. Другие необязательные коллекции перечислены в [CATALOG.md](CATALOG.md).

## Проверка

```bash
python3 -m unittest tests.test_bundle -v
```

Проверка подтверждает точный состав из 21 скилла, структуру frontmatter, навигатор, архитектуру, отсутствие приватных маркеров и запрещенных материалов.

## Авторы и лицензии

Часть скиллов создана внутри проекта, часть взята из открытых коллекций. Источники и лицензии перечислены в [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
