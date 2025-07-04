from importlib.metadata import version

from .classify import llm_classify, run_evals
from .default_templates import (
    CODE_FUNCTIONALITY_PROMPT_RAILS_MAP,
    CODE_FUNCTIONALITY_PROMPT_TEMPLATE,
    CODE_READABILITY_PROMPT_RAILS_MAP,
    CODE_READABILITY_PROMPT_TEMPLATE,
    HALLUCINATION_PROMPT_RAILS_MAP,
    HALLUCINATION_PROMPT_TEMPLATE,
    HUMAN_VS_AI_PROMPT_RAILS_MAP,
    HUMAN_VS_AI_PROMPT_TEMPLATE,
    QA_PROMPT_RAILS_MAP,
    QA_PROMPT_TEMPLATE,
    RAG_RELEVANCY_PROMPT_RAILS_MAP,
    RAG_RELEVANCY_PROMPT_TEMPLATE,
    REFERENCE_LINK_CORRECTNESS_PROMPT_RAILS_MAP,
    REFERENCE_LINK_CORRECTNESS_PROMPT_TEMPLATE,
    SQL_GEN_EVAL_PROMPT_RAILS_MAP,
    SQL_GEN_EVAL_PROMPT_TEMPLATE,
    TOOL_CALLING_PROMPT_RAILS_MAP,
    TOOL_CALLING_PROMPT_TEMPLATE,
    TOXICITY_PROMPT_RAILS_MAP,
    TOXICITY_PROMPT_TEMPLATE,
    USER_FRUSTRATION_PROMPT_RAILS_MAP,
    USER_FRUSTRATION_PROMPT_TEMPLATE,
)
from .evaluators import (
    HallucinationEvaluator,
    LLMEvaluator,
    QAEvaluator,
    RelevanceEvaluator,
    SQLEvaluator,
    SummarizationEvaluator,
    ToxicityEvaluator,
)
from .generate import llm_generate
from .models import (
    AnthropicModel,
    BedrockModel,
    GeminiModel,
    LiteLLMModel,
    MistralAIModel,
    OpenAIModel,
    VertexAIModel,
)
from .retrievals import compute_precisions_at_k
from .span_templates import (
    HALLUCINATION_SPAN_PROMPT_TEMPLATE,
    QA_SPAN_PROMPT_TEMPLATE,
    TOOL_CALLING_SPAN_PROMPT_TEMPLATE,
)
from .templates import (
    ClassificationTemplate,
    PromptTemplate,
)
from .utils import NOT_PARSABLE, download_benchmark_dataset

__version__ = version("arize-phoenix-evals")

__all__ = [
    "compute_precisions_at_k",
    "download_benchmark_dataset",
    "llm_classify",
    "llm_generate",
    "OpenAIModel",
    "AnthropicModel",
    "GeminiModel",
    "VertexAIModel",
    "BedrockModel",
    "LiteLLMModel",
    "MistralAIModel",
    "PromptTemplate",
    "ClassificationTemplate",
    "CODE_READABILITY_PROMPT_RAILS_MAP",
    "CODE_READABILITY_PROMPT_TEMPLATE",
    "HALLUCINATION_PROMPT_RAILS_MAP",
    "HALLUCINATION_PROMPT_TEMPLATE",
    "RAG_RELEVANCY_PROMPT_RAILS_MAP",
    "RAG_RELEVANCY_PROMPT_TEMPLATE",
    "TOXICITY_PROMPT_RAILS_MAP",
    "TOXICITY_PROMPT_TEMPLATE",
    "HUMAN_VS_AI_PROMPT_RAILS_MAP",
    "HUMAN_VS_AI_PROMPT_TEMPLATE",
    "REFERENCE_LINK_CORRECTNESS_PROMPT_RAILS_MAP",
    "REFERENCE_LINK_CORRECTNESS_PROMPT_TEMPLATE",
    "QA_PROMPT_RAILS_MAP",
    "QA_PROMPT_TEMPLATE",
    "SQL_GEN_EVAL_PROMPT_RAILS_MAP",
    "SQL_GEN_EVAL_PROMPT_TEMPLATE",
    "CODE_FUNCTIONALITY_PROMPT_RAILS_MAP",
    "CODE_FUNCTIONALITY_PROMPT_TEMPLATE",
    "USER_FRUSTRATION_PROMPT_RAILS_MAP",
    "USER_FRUSTRATION_PROMPT_TEMPLATE",
    "TOOL_CALLING_PROMPT_TEMPLATE",
    "TOOL_CALLING_PROMPT_RAILS_MAP",
    "NOT_PARSABLE",
    "run_evals",
    "LLMEvaluator",
    "HallucinationEvaluator",
    "QAEvaluator",
    "RelevanceEvaluator",
    "SQLEvaluator",
    "SummarizationEvaluator",
    "ToxicityEvaluator",
    "HALLUCINATION_SPAN_PROMPT_TEMPLATE",
    "QA_SPAN_PROMPT_TEMPLATE",
    "TOOL_CALLING_SPAN_PROMPT_TEMPLATE",
]
