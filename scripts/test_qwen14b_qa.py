from backend.app.llm.mlx_client import MLXClient


client = MLXClient()

prompt = r"""
You are a Senior QA Automation Engineer reviewing a failing test.

IMPORTANT:
Do not assume that making the test pass means the fix is correct.

Failure:
Expected: "Rp 5000000"
Actual:   "Rp5000000"

Relevant code:

const actualAmount = await transferPage.getAmountConfirmation();

// Convert actualAmount and expected amount to string and normalize the format
const formattedActualAmount = actualAmount.replace(/\./g, '');

// Convert number to string and remove separators if present
const formattedExpectedAmount =
  "Rp" + String(globalVariable.transfer.amount).replace(/\./g, '');

I.assertEqual(formattedActualAmount, formattedExpectedAmount);

Repository evidence:
The Konfirmasi Transfer screen is documented in the codebase as rendering currency with a space after "Rp", for example:
"Rp 15.000.000"

Do NOT modify any files.

Analyze both possible fixes:

A. Normalize the actual value:
actualAmount.replace(/[.\s]/g, '')

B. Change the expected value:
"Rp " + String(globalVariable.transfer.amount).replace(/\./g, '')

For each option explain:
1. What changes
2. Why the test would pass
3. Whether it preserves the intended test semantics
4. Risks of masking a real application defect

Then choose the safer fix based only on the evidence provided.

Return:
- Root cause
- Recommended fix
- Reason
- Risk
- Validation
"""

answer = client.chat(
    prompt,
    temperature=0.1,
    max_tokens=1024,
)

print("=" * 60)
print("QWEN 14B QA RCA")
print("=" * 60)
print(answer)