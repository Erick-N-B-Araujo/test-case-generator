@echo off

set content_type="Content-Type: application/json"
set token=%1
set token=%token:'=%
set authorization="Authorization: Bearer %token%"
set suite_id=%2
set suite_id=%suite_id:'=%
set scenario_id=%3
set scenario_id=%scenario_id:'=%
curl -X POST https://testesuaapi.ftabb.intranet.bb.com.br/api/cenarios/%scenario_id%/clonar/%suite_id% -H %content_type% -H %authorization%