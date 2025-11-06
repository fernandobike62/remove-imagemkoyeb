# 🖼️ Remove Background API (Rembg + FastAPI)

API simples que usa `rembg` para remover o fundo de imagens.

## 🚀 Deploy no Koyeb

1. Crie um novo repositório no GitHub e envie estes arquivos.
2. No [Koyeb](https://www.koyeb.com), clique em **Create App**.
3. Escolha **GitHub → selecione este repositório**.
4. Deploy automático (sem precisar configurar nada).
5. Após o deploy, sua API estará disponível em um link do tipo:

   ```
   https://seuapp.koyeb.app/remove-bg
   ```

## 📦 Endpoints

- **POST /remove-bg**
  - Envie uma imagem (campo `file`).
  - Retorna a imagem com o fundo removido (PNG).

## 🧠 Exemplo de uso (Python)

```python
import requests

with open("foto.jpg", "rb") as f:
    resp = requests.post("https://seuapp.koyeb.app/remove-bg", files={"file": f})
    open("foto_sem_fundo.png", "wb").write(resp.content)
```
