import json

from parking_data import new_state

_STORAGE_KEY = "click_vagas_state_v1"


async def carregar_estado(preferencias):
    salvo = await preferencias.get(_STORAGE_KEY)
    if isinstance(salvo, str):
        try:
            estado = json.loads(salvo)
            if isinstance(estado, dict) and isinstance(estado.get("usuarios"), dict) and isinstance(estado.get("vagas"), list):
                return estado
        except json.JSONDecodeError:
            pass
    estado = new_state()
    await salvar_estado(preferencias, estado)
    return estado


async def salvar_estado(preferencias, estado):
    await preferencias.set(_STORAGE_KEY, json.dumps(estado, ensure_ascii=False))
