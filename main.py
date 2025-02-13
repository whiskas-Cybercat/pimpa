from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def helius_webhook(request: Request):
    data = await request.json()
    print("Received Webhook:", data)  # Здесь можно добавить сохранение в базу данных
    return {"message": "Webhook received successfully"}
