from backend.app.llm.mlx_client import MLXClient

client = MLXClient()

print("=" * 60)
print("MODEL")
print("=" * 60)

print(client.health())

print()

print("=" * 60)
print("CHAT")
print("=" * 60)

answer = client.chat(
    "Reply only with the word SUCCESS."
)

print(answer)