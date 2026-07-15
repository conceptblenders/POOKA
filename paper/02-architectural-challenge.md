# 2. The Architectural Challenge

The emergence of Large Language Models has fundamentally changed the way humans interact with information. Rather than retrieving information through predefined interfaces, AI enables users to engage in natural language conversations capable of reasoning, summarizing, generating and transforming knowledge.

Despite these advances, the underlying organization of information has changed far less than the interaction itself. Most information remains fragmented across documents, applications, cloud services, conversations and personal notes. Structure, meaning and governance are often implicit, requiring AI to reconstruct them during every interaction.

As a consequence, collaboration increasingly depends on prompt engineering. Prompts establish roles, objectives, behavioral expectations, terminology, context and relevant background information at runtime. While this approach is flexible and often highly effective, it also produces context that is transient, difficult to maintain and challenging to reuse consistently across conversations, AI models and technical environments.

In architectural terms, a prompt is the means by which context and behavior are supplied to an AI system at the moment of interaction, and prompt engineering is the practice of constructing these instructions. Understood in this way, a prompt is a runtime carrier of context rather than a persistent part of the information architecture.

POOKA therefore interprets the growing importance of prompt engineering not as an architectural solution, but as an architectural symptom: it suggests the absence of persistent structures capable of representing meaning, context, governance and behavior independently of individual conversations.

Human collaboration rarely depends on repeatedly explaining identity, responsibilities, terminology or organizational context before every interaction. These elements persist beyond individual conversations and form part of a shared understanding. POOKA assumes that Human–AI collaboration requires similar persistence if it is to scale beyond isolated interactions.

POOKA is based on the assumption that this challenge is not primarily technological. More capable AI models reduce many limitations of reasoning, language understanding and generation, but they are not expected to eliminate the need for explicit organization of information. On this view, improvements in AI performance complement rather than replace information architecture.

POOKA approaches this challenge by treating information architecture as the primary carrier of context. Rather than reconstructing architectural knowledge through prompts, POOKA defines persistent architectural concepts that can be interpreted consistently by both humans and AI.

In this paper, persistence refers to the architectural representation of such concepts rather than to their content. A Context, for example, is represented persistently as part of the information architecture, while the Context itself remains adaptive and continues to evolve as work, conversations and objectives change. Persistent therefore means explicitly represented and maintained across interactions, rather than static.

The architectural challenge addressed by POOKA is therefore not how to create better prompts, but how to design information environments in which prompts become consumers of architecture rather than its primary source. This contrast is illustrated in Figure 1 (diagrams/prompt-vs-architecture.drawio).