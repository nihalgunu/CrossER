# CrossER Baselines To Run

## Completed

| Model | Context | F1 | Precision | Recall |
|-------|---------|-----|-----------|--------|
| — | String matching | 0.000 | 0.000 | 0.000 |
| — | Attribute matching | 0.145 | 0.080 | 0.783 |
| Claude Sonnet 4 | Zero-shot | 0.090 | 0.143 | 0.065 |

---

## To Run: Zero-shot (No Context)

Establishes floor for each model.

| Model | Provider | Est. Cost | Command |
|-------|----------|-----------|---------|
| GPT-4o | OpenAI | ~$2 | `python llm_baseline.py --provider openai --model gpt-4o --mechanism no_context` |
| GPT-4o-mini | OpenAI | ~$0.20 | `python llm_baseline.py --provider openai --model gpt-4o-mini --mechanism no_context` |
| o1 | OpenAI | ~$15 | `python llm_baseline.py --provider openai --model o1 --mechanism no_context` |
| Gemini 2.0 Flash | Google | ~$0.50 | Need to add provider |

---

## To Run: RAG (With Context)

Tests context retrieval mechanisms.

| Model | Context | Est. Cost | Notes |
|-------|---------|-----------|-------|
| Claude Sonnet 4 | RAG (top-10) | ~$3 | Need to implement RAG retrieval |
| GPT-4o | RAG (top-10) | ~$3 | Need to implement RAG retrieval |
| Claude Sonnet 4 | RAG (top-20) | ~$4 | Larger context window |
| GPT-4o | RAG (top-20) | ~$4 | Larger context window |

---

## Implementation Needed

### 1. RAG Retrieval (`rag_retrieval.py`)
```python
# Embed context items
# For each pair, retrieve top-k relevant context
# Pass to LLM with entity pair
```

### 2. Additional Providers
- Google (Gemini)
- OpenAI o1 (may need different API params)

---

## Priority Order

1. **GPT-4o zero-shot** — Compare to Claude
2. **o1 zero-shot** — See if reasoning helps
3. **Implement RAG** — Enable context experiments
4. **Claude + RAG** — First context baseline
5. **GPT-4o + RAG** — Compare models with context

---

## Run Commands

```bash
# Set API keys
export ANTHROPIC_API_KEY=...
export OPENAI_API_KEY=...

# Zero-shot baselines
python llm_baseline.py --provider openai --model gpt-4o --mechanism no_context
python llm_baseline.py --provider openai --model gpt-4o-mini --mechanism no_context

# RAG baselines (after implementation)
python llm_baseline.py --provider anthropic --mechanism rag
python llm_baseline.py --provider openai --model gpt-4o --mechanism rag
```
