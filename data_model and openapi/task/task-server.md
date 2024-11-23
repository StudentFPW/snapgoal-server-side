## Data types

| Database | Data Type (object_type) | Description |
|----------|-------------------------|-------------|
| Project  | project                 | Represents a project|
| Team     | team                    | Represents a team|
| Task    | task                   | Represents a level |

## Object: project

A project encompasses multiple teams, levels, and tasks. This object defines the project's overall structure and details.

| Naming            | Description                                                        | Type                | Unique | Required |
|-------------------|--------------------------------------------------------------------|---------------------|--------|----------|
| object_type       | The type of the object, which is 'project' in this case.            | String 'project'    | No     | Yes      |
| **Attributes (data)** |                                                             |                     |        |          |
| title             | The name of the project. This helps identify the project.          | string              | No     | Yes      |
| description       | A detailed description of the project, outlining its goals and objectives. | string              | No     | No       |
| start_date        | The start date of the project.                                      | date                | No     | Yes      |
| end_date          | The planned end date of the project.                                | date                | No     | No       |
| status            | The current status of the project (e.g., "active", "completed", "on hold"). | string              | No     | Yes      |
| teams             | A list of teams within the project. Each team has its own set of members and tasks. | array of strings    | No     | No       |

## Object: team

A team is a group of members working together on tasks within a project. This object defines the structure of a team and the tasks it is working on.

| Naming            | Description                                                        | Type                | Unique | Required |
|-------------------|--------------------------------------------------------------------|---------------------|--------|----------|
| object_type       | The type of the object, which is 'team' in this case.               | String 'team'       | No     | Yes      |
| **Attributes (data)** |                                                             |                     |        |          |
| title             | The name of the level (e.g., "Phase 1", "Critical Tasks").          | string              | No     | Yes      |
| members           | A list of member IDs or references that belong to this team.       | array of strings    | No     | Yes      |
| tasks            | A list of tasks within the project that organize tasks by stages or priority. | array of strings    | No     | No       |                   | date                | No     | Yes      |

## Object: task

A task represents an individual unit of work that needs to be completed within a project. Tasks are typically linked to specific levels or stages within the project and can have dependencies, assignees, and other metadata that help manage the project flow.

| Naming            | Description                                                        | Type                | Unique | Required |
|-------------------|--------------------------------------------------------------------|---------------------|--------|----------|
| object_type       | The type of the object, which is 'task' in this case.               | String 'task'       | No     | Yes      |
| **Attributes (data)** |                                                             |                     |        |          |
| title             | The name or title of the task. This helps identify the task in the task board. | string              | No     | Yes      |
| description       | A detailed description of the task, providing more information about what needs to be done. | string              | No     | No       |
| image             | A URL link to an image or icon associated with the task. This could be used to visually represent the task. | string (e.g., "1Y" or "O.5Y") | No     | Yes      |
| feedback          | The type of period calculation for the task's progress. It can either be "sliding" (progress based on a moving timeframe) or "fixed" (based on a static start date). | sliding/fixed       | No     | Yes      |
| badge_id          | An identifier for the type of badge associated with the task, indicating a specific task status or category (e.g., "urgent", "low priority"). | string              | No     | Yes      |
| priority          | The priority of the task, helping to determine the order in which tasks should be addressed (e.g., "high", "medium", "low"). | string              | No     | Yes      |
| status            | The current status of the task (e.g., "not started", "in progress", "completed", "on hold"). | string              | No     | Yes      |
| start_date        | The start date of the task, indicating when work on the task is scheduled to begin. | date                | No     | Yes      |
| due_date          | The due date of the task, indicating when the task should be completed. | date                | No     | Yes      |
| assignee_id       | The ID of the person or team assigned to work on this task. Can be linked to a **member** or **team** object. | string              | No     | Yes      |