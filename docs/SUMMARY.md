# Table of contents

* [Arize Phoenix](README.md)
* [Quickstarts](quickstart.md)
* [User Guide](user-guide.md)
* [Deployment](deployment.md)
* [Environments](environments.md)
* [Phoenix Demo](https://phoenix-demo.arize.com/projects)

## 🔭 Tracing

* [Overview: Tracing](tracing/llm-traces.md)
* [Quickstart: Tracing](tracing/llm-traces-1/README.md)
  * [Quickstart: Tracing (Python)](tracing/llm-traces-1/quickstart-tracing-python.md)
  * [Quickstart: Tracing (TS)](tracing/llm-traces-1/quickstart-tracing-ts.md)
* [Features: Tracing](tracing/features-tracing/README.md)
  * [Projects](tracing/features-tracing/projects.md)
  * [Annotations](tracing/features-tracing/how-to-annotate-traces.md)
  * [Sessions](tracing/features-tracing/sessions.md)
* [Integrations: Tracing](tracing/integrations-tracing/README.md)
  * [OpenAI](tracing/integrations-tracing/openai.md)
  * [OpenAI Agents SDK](tracing/integrations-tracing/openai-agents-sdk.md)
  * [LlamaIndex](tracing/integrations-tracing/llamaindex.md)
  * [LlamaIndex Workflows](tracing/integrations-tracing/llamaindex-1.md)
  * [LangChain](tracing/integrations-tracing/langchain.md)
  * [LangGraph](tracing/integrations-tracing/langgraph.md)
  * [LiteLLM](tracing/integrations-tracing/litellm.md)
  * [Anthropic](tracing/integrations-tracing/anthropic.md)
  * [Amazon Bedrock](tracing/integrations-tracing/bedrock.md)
  * [Amazon Bedrock Agents](tracing/integrations-tracing/bedrock-1.md)
  * [VertexAI](tracing/integrations-tracing/vertexai.md)
  * [Agno](tracing/integrations-tracing/agno.md)
  * [Model Context Protocol (MCP)](tracing/integrations-tracing/model-context-protocol-mcp.md)
  * [MistralAI](tracing/integrations-tracing/mistralai.md)
  * [Google GenAI](tracing/integrations-tracing/google-genai.md)
  * [Groq](tracing/integrations-tracing/groq.md)
  * [Hugging Face smolagents](tracing/integrations-tracing/hfsmolagents.md)
  * [CrewAI](tracing/integrations-tracing/crewai.md)
  * [Haystack](tracing/integrations-tracing/haystack.md)
  * [DSPy](tracing/integrations-tracing/dspy.md)
  * [Instructor](tracing/integrations-tracing/instructor.md)
  * [OpenAI Node SDK](tracing/integrations-tracing/openai-node-sdk.md)
  * [LangChain.js](tracing/integrations-tracing/langchain.js.md)
  * [Vercel AI SDK](tracing/integrations-tracing/vercel-ai-sdk.md)
  * [LangFlow](tracing/integrations-tracing/langflow.md)
  * [BeeAI](tracing/integrations-tracing/beeai.md)
  * [Flowise](tracing/integrations-tracing/flowise.md)
  * [Prompt flow](tracing/integrations-tracing/prompt-flow.md)
  * [AutoGen](tracing/integrations-tracing/autogen-support.md)
  * [Guardrails AI](tracing/integrations-tracing/guardrails-ai.md)
* [How-to: Tracing](tracing/how-to-tracing/README.md)
  * [Setup Tracing](tracing/how-to-tracing/setup-tracing/README.md)
    * [Setup using Phoenix OTEL](tracing/how-to-tracing/setup-tracing/setup-using-phoenix-otel.md)
    * [Setup using base OTEL](tracing/how-to-tracing/setup-tracing/custom-spans.md)
    * [Using Phoenix Decorators](tracing/how-to-tracing/setup-tracing/instrument-python.md)
    * [Setup Tracing (TS)](tracing/how-to-tracing/setup-tracing/javascript.md)
    * [Setup Projects](tracing/how-to-tracing/setup-tracing/setup-projects.md)
    * [Setup Sessions](tracing/how-to-tracing/setup-tracing/setup-sessions.md)
  * [Add Metadata](tracing/how-to-tracing/add-metadata/README.md)
    * [Add Attributes, Metadata, Users](tracing/how-to-tracing/add-metadata/customize-spans.md)
    * [Instrument Prompt Templates and Prompt Variables](tracing/how-to-tracing/add-metadata/instrumenting-prompt-templates-and-prompt-variables.md)
  * [Annotate Traces](tracing/how-to-tracing/feedback-and-annotations/README.md)
    * [Annotating in the UI](tracing/how-to-tracing/feedback-and-annotations/annotating-in-the-ui.md)
    * [Annotating via the Client](tracing/how-to-tracing/feedback-and-annotations/capture-feedback.md)
    * [Annotating Auto-Instrumented Spans](tracing/how-to-tracing/feedback-and-annotations/annotating-auto-instrumented-spans.md)
    * [Running Evals on Traces](tracing/how-to-tracing/feedback-and-annotations/evaluating-phoenix-traces.md)
    * [Log Evaluation Results](tracing/how-to-tracing/feedback-and-annotations/llm-evaluations.md)
  * [Importing & Exporting Traces](tracing/how-to-tracing/importing-and-exporting-traces/README.md)
    * [Import Existing Traces](tracing/how-to-tracing/importing-and-exporting-traces/importing-existing-traces.md)
    * [Export Data & Query Spans](tracing/how-to-tracing/importing-and-exporting-traces/extract-data-from-spans.md)
    * [Exporting Annotated Spans](tracing/how-to-tracing/importing-and-exporting-traces/exporting-annotated-spans.md)
  * [Advanced](tracing/how-to-tracing/advanced/README.md)
    * [Mask Span Attributes](tracing/how-to-tracing/advanced/masking-span-attributes.md)
    * [Suppress Tracing](tracing/how-to-tracing/advanced/suppress-tracing.md)
    * [Filter Spans to Export](tracing/how-to-tracing/advanced/modifying-spans.md)
    * [Capture Multimodal Traces](tracing/how-to-tracing/advanced/multimodal-tracing.md)

## 📃 Prompt Engineering

* [Overview: Prompts](prompt-engineering/overview-prompts.md)
  * [Prompt Management](prompt-engineering/overview-prompts/prompt-management.md)
  * [Prompt Playground](prompt-engineering/overview-prompts/prompt-playground.md)
  * [Span Replay](prompt-engineering/overview-prompts/span-replay.md)
  * [Prompts in Code](prompt-engineering/overview-prompts/prompts-in-code.md)
* [Quickstart: Prompts](prompt-engineering/quickstart-prompts/README.md)
  * [Quickstart: Prompts (UI)](prompt-engineering/quickstart-prompts/quickstart-prompts-ui.md)
  * [Quickstart: Prompts (Python)](prompt-engineering/quickstart-prompts/quickstart-prompts-python.md)
  * [Quickstart: Prompts (TS)](prompt-engineering/quickstart-prompts/quickstart-prompts-ts.md)
* [How to: Prompts](prompt-engineering/how-to-prompts/README.md)
  * [Configure AI Providers](prompt-engineering/how-to-prompts/configure-ai-providers.md)
  * [Using the Playground](prompt-engineering/how-to-prompts/using-the-playground.md)
  * [Create a prompt](prompt-engineering/how-to-prompts/create-a-prompt.md)
  * [Test a prompt](prompt-engineering/how-to-prompts/test-a-prompt.md)
  * [Tag a prompt](prompt-engineering/how-to-prompts/tag-a-prompt.md)
  * [Using a prompt](prompt-engineering/how-to-prompts/using-a-prompt.md)
* [Concepts: Prompts](prompt-engineering/concepts-prompts.md)

## 🗄️ Datasets & Experiments

* [Overview: Datasets & Experiments](datasets-and-experiments/overview-datasets.md)
* [Quickstart: Datasets & Experiments](datasets-and-experiments/quickstart-datasets.md)
* [How-to: Datasets](datasets-and-experiments/how-to-datasets/README.md)
  * [Creating Datasets](datasets-and-experiments/how-to-datasets/creating-datasets.md)
  * [Exporting Datasets](datasets-and-experiments/how-to-datasets/exporting-datasets.md)
* [Concepts: Datasets](datasets-and-experiments/concepts-datasets.md)
* [How-to: Experiments](datasets-and-experiments/how-to-experiments/README.md)
  * [Run Experiments](datasets-and-experiments/how-to-experiments/run-experiments.md)
  * [Using Evaluators](datasets-and-experiments/how-to-experiments/using-evaluators.md)

## 🧠 Evaluation

* [Overview: Evals](evaluation/llm-evals/README.md)
  * [Agent Evaluation](evaluation/llm-evals/agent-evaluation.md)
* [Quickstart: Evals](evaluation/evals.md)
* [How to: Evals](evaluation/how-to-evals/README.md)
  * [Pre-Built Evals](evaluation/how-to-evals/running-pre-tested-evals/README.md)
    * [Hallucinations](evaluation/how-to-evals/running-pre-tested-evals/hallucinations.md)
    * [Q\&A on Retrieved Data](evaluation/how-to-evals/running-pre-tested-evals/q-and-a-on-retrieved-data.md)
    * [Retrieval (RAG) Relevance](evaluation/how-to-evals/running-pre-tested-evals/retrieval-rag-relevance.md)
    * [Summarization](evaluation/how-to-evals/running-pre-tested-evals/summarization-eval.md)
    * [Code Generation](evaluation/how-to-evals/running-pre-tested-evals/code-generation-eval.md)
    * [Toxicity](evaluation/how-to-evals/running-pre-tested-evals/toxicity.md)
    * [AI vs Human (Groundtruth)](evaluation/how-to-evals/running-pre-tested-evals/ai-vs-human-groundtruth.md)
    * [Reference (citation) Link](evaluation/how-to-evals/running-pre-tested-evals/reference-link-evals.md)
    * [User Frustration](evaluation/how-to-evals/running-pre-tested-evals/user-frustration.md)
    * [SQL Generation Eval](evaluation/how-to-evals/running-pre-tested-evals/sql-generation-eval.md)
    * [Agent Function Calling Eval](evaluation/how-to-evals/running-pre-tested-evals/tool-calling-eval.md)
    * [Agent Path Convergence](evaluation/how-to-evals/running-pre-tested-evals/agent-path-convergence.md)
    * [Agent Planning](evaluation/how-to-evals/running-pre-tested-evals/agent-planning.md)
    * [Agent Reflection](evaluation/how-to-evals/running-pre-tested-evals/agent-reflection.md)
    * [Audio Emotion Detection](evaluation/how-to-evals/running-pre-tested-evals/audio-emotion-detection.md)
  * [Eval Models](evaluation/how-to-evals/evaluation-models.md)
  * [Build an Eval](evaluation/how-to-evals/bring-your-own-evaluator.md)
  * [Build a Multimodal Eval](evaluation/how-to-evals/multimodal-evals.md)
  * [Online Evals](evaluation/how-to-evals/online-evals.md)
  * [Evals API Reference](evaluation/how-to-evals/evals-reference.md)
* [Concepts: Evals](evaluation/concepts-evals/README.md)
  * [LLM as a Judge](evaluation/concepts-evals/llm-as-a-judge.md)
  * [Eval Data Types](evaluation/concepts-evals/evaluation-types.md)
  * [Evals With Explanations](evaluation/concepts-evals/evals-with-explanations.md)
  * [Evaluators](evaluation/concepts-evals/evaluation.md)
  * [Custom Task Evaluation](evaluation/concepts-evals/building-your-own-evals.md)

## 🔍 Retrieval

* [Overview: Retrieval](retrieval/overview-retrieval.md)
* [Quickstart: Retrieval](retrieval/quickstart-retrieval.md)
* [Concepts: Retrieval](retrieval/concepts-retrieval/README.md)
  * [Retrieval with Embeddings](retrieval/concepts-retrieval/troubleshooting-llm-retrieval-with-vector-stores.md)
  * [Benchmarking Retrieval](retrieval/concepts-retrieval/benchmarking-retrieval-rag.md)
  * [Retrieval Evals on Document Chunks](retrieval/concepts-retrieval/retrieval-evals-on-document-chunks.md)

## 🌌 inferences

* [Quickstart: Inferences](inferences/phoenix-inferences.md)
* [How-to: Inferences](inferences/how-to-inferences/README.md)
  * [Import Your Data](inferences/how-to-inferences/define-your-schema/README.md)
    * [Prompt and Response (LLM)](inferences/how-to-inferences/define-your-schema/prompt-and-response-llm.md)
    * [Retrieval (RAG)](inferences/how-to-inferences/define-your-schema/retrieval-rag.md)
    * [Corpus Data](inferences/how-to-inferences/define-your-schema/corpus-data.md)
  * [Export Data](inferences/how-to-inferences/export-your-data.md)
  * [Generate Embeddings](inferences/how-to-inferences/generating-embeddings.md)
  * [Manage the App](inferences/how-to-inferences/manage-the-app.md)
  * [Use Example Inferences](inferences/how-to-inferences/use-example-inferences.md)
* [Concepts: Inferences](inferences/inferences.md)
* [API: Inferences](inferences/inference-and-schema.md)
* [Use-Cases: Inferences](inferences/use-cases-inferences/README.md)
  * [Embeddings Analysis](inferences/use-cases-inferences/embeddings-analysis.md)

## 🔌 INTEGRATIONS

* [Phoenix MCP Server](integrations/phoenix-mcp-server.md)
* [Cleanlab](integrations/cleanlab.md)
* [Ragas](integrations/ragas.md)

## ⚙️ Settings

* [Access Control (RBAC)](settings/access-control-rbac.md)
* [API Keys](settings/api-keys.md)
* [Data Retention](settings/data-retention.md)
