## Data storage registries

| Registry | Purpose |
|--------|-----------|
| Rating | Rating configurations and calculated ratings |
| Result | Participant results |

## Data types in registries

| Registry | Data type (object_type) | Description |
|--------|------------|------------------------|
| Rating | rating | Rules by which we evaluate rating participants |
| Rating | competition | Calculated ratings |
| Result | - | Result of a participant (person, team, etc.) |

## Object: rating
Rules by which we evaluate participants.

| Name | Purpose | Format | Unique | Mandatory |
|---------------|-----------------------------------------------------------|-----------------------|-----------|-------------|
| object_code | Unique rating code | String like `<project_id>:<code>` | Yes | Yes |
| object_type | Record type | String 'rating' | No | Yes |
| Field **data**: | | | |
| position | Array of intervals | [[1, 10], [11, 100], [101, 500], [501, 1000], [1001, 5000], # continued...] | No | Yes |
| order | Determines the sorting order of the array of intervals | asc/desc | No | Yes |
| period | Time range for calculating the rating | String (e.g. "1Y" OR "O.5Y") | No | Yes |
| period_type | Period calculation type: sliding or from the beginning of the period | slidding/fixed | No | Yes |

## Object: competition
Calculated rankings. Each object can have different data, including time or numeric ranges.

| Name | Purpose | Format | Unique | Required |
|--------------|------------------------------------------------------------|------------------------|------------|--------------|
| object_type | Record type | String 'competition' | No | Yes |
| object_item | ID of the configuration on which the ranking is calculated | uuid | Yes | Yes |
| Field **data**: | | | |
| interval | Data about the results and their corresponding places | `{position : [ [1,10],[11, 100]],place_result : [[1.2, 1.9],[2.5, 2.14], [5.1, 5.3]]}`| No | Yes |
| from_date | Start date of the time interval for which the rating is calculated | Date and time | No | Yes |
| to_date | End date of the time interval for which the rating is calculated | Date and time | No | Yes |

## Object: result
Participants' results.

| Name | Purpose | Format | Unique | Required |
|---------------|------------------------------------------------------------|-----------------------|------------|-------------|
| account_id | Participant group (team) identifier | uuid| No | No |
| user_id | Member ID | uuid| No | No |
| object_type | Result data type | String | No | No|
| object_item | Organization ID | uuid | No | Yes |
| Field **data**: ||||
| result | Member Result | String | No | Yes |
| date | Result date| Date and time | No | Yes |
