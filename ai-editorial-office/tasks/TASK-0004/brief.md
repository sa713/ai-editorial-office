# Brief

Task ID: `TASK-0004`

Owner: `intake_agent`

Stage: `intake`

## source

Primary source file: `/tasks/TASK-0004/source-draft.md`

Note: the file has docx/zip structure despite the `.md` extension. Text was extracted for review with `pandoc -f docx -t markdown`.

## task

Review and improve a draft instruction for using an internal task exchange.

The instruction must help employees understand what to do, in what order, under which constraints, and who owns each action.

## primary reader task

The reader needs to use the task exchange as one of these roles:

- create and manage a task as Author;
- respond to and execute a task as Executor;
- submit an idea;
- understand when Moderators or Curators are involved.

## likely reader state

- busy and trying to complete a practical action;
- unfamiliar with the pilot process or with how Taska is adapted for this use;
- likely to scan by role rather than read the whole document;
- sensitive to unclear ownership, unclear sequence, and missing next step.

## operational goal

After reading, the employee should know:

- which section applies to them;
- what to fill in;
- what not to fill in;
- what happens after submission;
- who moves the card or makes the next decision;
- where to go when the process is disputed or unclear.

## critical misunderstanding risks

- User may not understand the difference between `Задача` and `Идея`.
- Author may think moderation automatically assigns an executor.
- Executor may think leaving a comment is enough to start work before Author selection.
- Author may not know they own executor selection and completion check.
- Reader may miss the ban on subtasks.
- Reader may not know what to do with `Мои задачи`.
- Source draft contains an undefined `Инициатива` term and an unfinished note inside the instruction.

## likely drop-off points

- Opening explains the system before giving reader routes.
- Terms table appears before the reader knows which action they need.
- Process overview and role-specific steps partially duplicate each other.
- `Мои задачи` section is unfinished and likely breaks trust.
- Dispute handling is too thin to be useful.

## success criteria

- Clear role-based navigation.
- Operational steps appear before optional background.
- Rules and constraints are visible near the action they affect.
- Sequence of task and idea flows remains intact.
- No motivational, HR-style, marketing, or platform-philosophy language.
- Ambiguity is not hidden; unsupported product specifics are not invented.
