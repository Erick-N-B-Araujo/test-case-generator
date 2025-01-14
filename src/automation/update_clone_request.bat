@echo off

set content_type="Content-Type: application/json"
set token=%1
set token=%token:'=%
set authorization="Authorization: Bearer %token%"
set suite_id=%2
set suite_id=%suite_id:'=%
set cloned_scenario_id=%3
set cloned_scenario_id=%cloned_scenario_id:'=%
set scenario_id=%4
set scenario_id=%scenario_id:'=%
set scenario_title=%5
set scenario_title=%scenario_title:"=%
set history_id=%6
set history_id=%history_id:'=%

curl -X PATCH https://testesuaapi.ftabb.intranet.bb.com.br/api/cenarios/%cloned_scenario_id% -H %content_type% -H %authorization% -d "{\"suiteId\": \"%suite_id%\",\"nome\": \"CT%scenario_id% - %scenario_title%\",\"historiaALM\": \"%history_id%\",\"tipoArtefato\": \"GENTI\"}"