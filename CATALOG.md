# Каталог проверенных коллекций скиллов

Отобранные и проверенные в работе коллекции скиллов для AI-агентов (Claude Code, Codex CLI и совместимые).
Все репозитории публичные, принадлежат своим авторам - здесь ссылки и навигация, что брать и зачем.


## ЗОЛОТОЙ НАБОР - с чего начинать (проверено в реальной работе)

Три яруса приоритета. Агент, подбирающий скиллы владельцу: иди сверху вниз, нижний ярус - только по явной надобности.

### Ярус 1 - ставить почти всем
- Этот кит: `slide-craft`, `data-analyst`, `meeting-insights`, `strategic-advisor` (папка `skills/`).
- anthropics/skills: `docx`, `xlsx`, `pptx`, `pdf` (работа с офисными файлами - нужна каждый день), `skill-creator`.
- obra/superpowers: `brainstorming`, `verification-before-completion`, `systematic-debugging`.

### Ярус 2 - золото по профилю
- **Дизайн/фронтенд:** pbakaus/impeccable (весь), emilkowalski `emil-design-eng` + `review-animations`, ui-ux-pro-max `ui-ux-pro-max` + `slides`, anthropics `frontend-design`.
- **Оркестрация и качество агентов:** ECC `loop-design-check`, `agent-harness-construction`, `agent-architecture-audit`, `santa-method`, `safety-guard`, `council`; mattpocock `grilling`, `handoff`, `teach`.
- **Безопасность (защитная):** trailofbits `differential-review`, `audit-context-building`; ECC `security-scan`.
- **Контент/маркетинг:** ECC `content-engine`, `brand-voice`; coreyhaines31/marketingskills - выборочно под канал.
- **Передача настроек людям:** mattpocock `wizard`, `to-questionnaire`.

### Ярус 3 - основная масса (по надобности)
Все остальное из SKILLS-LIST.md: стек-специфичные клоны (django/rust/kotlin...), нишевые вертикали
(homelab, healthcare, крипта, сети), Azure, самообслуживание ECC. Не ставь «на всякий случай» -
клонируй коллекцию и бери конкретный скилл, когда появилась конкретная задача.

## Как установить коллекцию

```bash
git clone --depth 1 https://github.com/<slug>.git
# скопируй нужные папки скиллов в ~/.claude/skills/ (Claude Code) и/или ~/.codex/skills/ (Codex)
```

## Дизайн и презентации

| Репозиторий | Что это |
|---|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Дизайн-язык против ИИ-слопа во фронтенде: polish, audit, critique, типографика. Автор - создатель jQuery UI |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Дизайн-инженерия и анимации от Emil Kowalski (Vercel/Linear): полировка UI, ревью анимаций, Apple-принципы |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | База дизайн-знаний: 84 стиля, 192 палитры, 74 пары шрифтов, 98 UX-правил + отдельный скилл slides |
| [jakubantalik/transitions-dev](https://github.com/jakubantalik/transitions-dev) | CSS-микроанимации |

## Официальное от Anthropic

| Репозиторий | Что это |
|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | Официальные скиллы: docx, xlsx, pptx, pdf, mcp-builder, skill-creator, webapp-testing, frontend-design и др. |

## Методология разработки и качество агентов

| Репозиторий | Что это |
|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | Полный цикл разработки: brainstorming, TDD, планы, ревью, отладка, верификация |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | ECC, победитель хакатона Anthropic: 183 скилла, 48 агентов, 79 команд. Золото: loop-design-check, santa-method, agent-harness-construction, safety-guard |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Инженерные скиллы Matt Pocock, кросс-средовые (Claude+Codex). Золото: grilling, handoff, teach, wizard |
| [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | Качество работы агентов, контекст-инжиниринг |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | find-skills: поиск нужного скилла из тысяч |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 83 совета по Claude Code |

## Безопасность

| Репозиторий | Что это |
|---|---|
| [trailofbits/skills](https://github.com/trailofbits/skills) | Аудит кода и поиск уязвимостей от Trail of Bits (защитное): differential-review, audit-context-building |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 750+ кибербез-скиллов. ВНИМАНИЕ: dual-use, держать изолированно, не ставить в рабочее ядро |

## Маркетинг и контент

| Репозиторий | Что это |
|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | CRO, копирайт, SEO, аналитика, рост |
| [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | SEO/GEO |

## Прочее

| Репозиторий | Что это |
|---|---|
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Мультиагентный фреймворк |
| [microsoft/azure-skills](https://github.com/microsoft/azure-skills) | Azure |
| [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | AI-видео стек (open-source) |

## Совет по установке

Не ставь все подряд: каждый установленный скилл добавляет свое описание в контекст каждой сессии.
Рабочее ядро держи компактным (30-70 скиллов под свои задачи), остальное - в локальном арсенале
и подключай по надобности. Обязательно заведи навигатор `_INDEX.md` в папке скиллов: одна строка
на скилл - «когда брать» и «что делает», и вшей агенту правило называть выбранные скиллы перед задачей.
