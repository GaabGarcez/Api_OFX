from fastapi import FastAPI, HTTPException, Request
import re

app = FastAPI()

@app.post("/convert")
async def convert_to_xml(request: Request):
    try:
        # Obter o corpo da solicitação como string
        ofx_data = await request.body()
        ofx_data = ofx_data.decode('utf-8')

        # Usar regex para extrair o conteúdo entre as tags <OFX></OFX>
        match = re.search(r'(<OFX>.*?</OFX>)', ofx_data, re.DOTALL)
        if match:
            xml_content = match.group(1).strip()
            return {"xml": xml_content}
        else:
            raise HTTPException(status_code=400, detail="Conteúdo OFX não encontrado")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
