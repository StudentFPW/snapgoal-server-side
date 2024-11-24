# Upload an image (only jpeg is supported):
```bash
curl -X POST -F file=@</home/...file_path....jpeg> https://snapgoal.org/badge
```
Response:
```json
{
    "uuid": "45b307a7-4354-46a6-bbcf-2c0cc5fb0a5d"
}
```
# Link to the uploadad image (only jpeg is supported):

https://snapgoal.org/badge/[uuid from the above command]

# Update badge information into the database:
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"uuid": "uuid from the above command", "title": "sample", "description":"sample description", "points": 3, "imageUrl": "https://snapgoal.org/badge/uuid from the above command"}' https://snapgoal.org/badge/<uuid from the above command>
```
# List all existing badges:
```bash
curl https://snapgoal.org/badge
```
Sample result:
```json
[
    {
        "description": "sample description",
        "id": "de3372b9-6c36-42a2-80fa-476725e184f6",
        "imageUrl": "https://snapgoal.org/badge/5dc13e03-848a-403a-b253-9cdc9667f0a4.jpeg",
        "points": 3,
        "title": "sample"
    }
]
```