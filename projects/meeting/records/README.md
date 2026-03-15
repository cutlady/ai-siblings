# 会议记录存放规则

## 📁 目录结构

```
meeting/records/
├── daily/           # 早会纪要（每天8:00）
│   └── YYYY-MM-DD.md
├── standup/         # 站会纪要（每天8:30）
│   └── YYYY-MM-DD.md
├── project/         # 项目例会纪要
│   └── YYYY-MM-DD-项目名.md
├── weekly/          # 周会纪要（每周日20:00）
│   └── YYYY-MM-DD-weekWW.md
└── monthly/         # 月会纪要（每月1号）
│   └── YYYY-MM-DD-monthMM.md
```

---

## 📝 命名规范

| 会议类型 | 文件名格式 | 示例 |
|----------|------------|------|
| 早会 | `YYYY-MM-DD.md` | `2026-03-15.md` |
| 站会 | `YYYY-MM-DD.md` | `2026-03-15.md` |
| 项目例会 | `YYYY-MM-DD-项目名.md` | `2026-03-15-99day.md` |
| 周会 | `YYYY-MM-DD-weekWW.md` | `2026-03-16-week11.md` |
| 月会 | `YYYY-MM-DD-monthMM.md` | `2026-04-01-month04.md` |

---

## 📋 项目例会说明

**触发条件**：
- 单个项目需要深度讨论
- 项目里程碑评审
- 项目遇到重大问题

**命名规则**：日期在前，项目代号在后

**存放位置**：`records/project/`

**关联**：在对应项目的 README 中链接到会议纪要

---

## 🔗 跨项目会议

如果会议涉及多个项目：
1. 在 `records/project/` 下创建会议纪要以日期命名
2. 在各项目的 README 中引用该会议
3. 在 PROJECTS.md 中更新相关项目状态

---

*最后更新：2026-03-15 by @王大虾*
