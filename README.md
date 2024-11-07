# AWS LAMBDA FUNCTION LOCAL

Reference Link: 
- https://docs.docker.com/compose/how-tos/file-watch/#action
- https://stackoverflow.com/questions/40905761/how-do-i-mount-a-host-directory-as-a-volume-in-docker-compose
- https://gallery.ecr.aws/lambda/python
- https://docs.docker.com/engine/storage/bind-mounts/

## Comandos utilizados
- `docker compose down`
- `docker-compose up --build --remove-orphans --force-recreate`
- `docker compose up --watch`

```powershell
curl -X POST http://localhost:8000/2015-03-31/functions/function/invocations `
>     -H 'Content-Type: application/json' `
>     -d (Get-Content -Raw -Path .\event.json) | python3 -m json.tool
```