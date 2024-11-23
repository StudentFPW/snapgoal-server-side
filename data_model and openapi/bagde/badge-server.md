## Data types

| Database | Data Type (object_type) | Description |
|----------|-------------------------|-------------|
| Badge  | bagde                 | Represents a bagde|

## Object: badge

A badge represents a special designation or achievement that can be assigned to tasks, projects, or members. It helps highlight specific statuses, milestones, or accomplishments within the project.

| Naming            | Description                                                        | Type                | Unique | Required |
|-------------------|--------------------------------------------------------------------|---------------------|--------|----------|
| object_type       | The type of the object, which is 'badge' in this case.              | String 'badge'      | No     | Yes      |
| **Attributes (data)** |                                                             |                     |        |          |
| title             | The name of the badge (e.g., "High Priority", "Completed", "Milestone Achiever"). | string              | Yes    | Yes      |
| description       | A detailed description of the badge, explaining its purpose or when it is awarded. | string              | No     | No       |
| points            | The number of points associated with the badge, representing the achievement level. | number (integer)    | No     | No       |
| image_url         | A URL link to an image or icon representing the badge.             | string (URL)        | No     | Yes      |
