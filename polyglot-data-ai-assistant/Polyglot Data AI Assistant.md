# Polyglot Data Assistant: Edge AI for Mobile 🚀

![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E?style=for-the-badge&logoColor=black)
![Llama](https://img.shields.io/badge/Llama_3.2-0467DF?style=for-the-badge&logo=meta&logoColor=white)
![Gemma](https://img.shields.io/badge/Gemma_2-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Qwen](https://img.shields.io/badge/Qwen_2.5-525CB0?style=for-the-badge&logo=alibabacloud&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![LLM](https://img.shields.io/badge/Local_LLM-FFD700?style=for-the-badge&logo=ai&logoColor=black)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

---

<details>
<summary>🇧🇷 <b>Português (Versão Original)</b></summary>

## Visão Geral
Este projeto demonstra a implementação de um assistente de IA **100% offline** em um dispositivo móvel. O objetivo é criar um tutor especializado em **Engenharia de Dados** e **Estudos Poliglotas**, otimizado para hardware restrito, garantindo privacidade e custo zero. 

## Detalhes
Eu gosto muito de idiomas e gosto muito da interação com IA. Os chatbots estão me ajudando muito com estudo de idiomas, aprendizado de novas palavras (ex.: caso esteja lendo um livro em inglês, posso perguntar sobre palavras no dado contexto, de modo que aprenda com a experiência cultural da IA para explicar de uma forma que apenas usando o Google Translate não seria possível, além também funcionar como um dicionário mais interativo) e programação ou consulta (ex.: qual comando xpto em Git para fazer uma mudança da branch main para outra branch, já criando a branch?).

Embora tenha assinatura mensal de uma IA para fins profissionais, pessoais e de estudos, sempre fiquei pensando como seria divertido ter minha própria IA no meu celular. Conversando com o Gemini, meu tutor, hehe, percebi que tudo estava mais simplificado do que imaginei! Descobri o MLC Chat, mas tive uns problemas, para encurtar o tempo, achei a solução perfeita com o ChatterUI, um projeto open-source que já oferta uma ótima aplicação de interface e permite que carreguemos modelos diretamente do Hugging Face! 

## Desenvolvendo o projeto
Bom, primeiro passo foi ter o APK do ChatterUI. Para isso, aqui está o link para o repositório oficial: [ChatterUI](https://github.com/Vali-98/ChatterUI). Basta baixar e instalar o .apk no Android (tenha em mente que as permissões adequadas devem estar habilitadas). Feito isso, teremos uma interface em que é possível criarmos um personagem ("Character"). Isso permite configurações de personalidade, limitação do escopo do modelo, etc. Para meu caso em particular, em que eu queria uma IA que servisse para usos de Engenharia de Dados com Python e SQL, além de me ajudar em meus estudos de inglês e chinês (o português entra como mecanismo de ser meu idioma nativo). 

![character_creation](https://github.com/user-attachments/assets/eaa77430-3cff-4d99-9360-e980ea5fbe83)
> Aqui passei os prompts para dar enfoque ao modelo para os meus objetivos.

Após essa fase de configuração do personagem (persona), utilizei o modelo, conforme na imagem (é necessário, ao selecionar o personagem, carregar o modelo desejado). Os modelos são carregados na seção "Models" do ChatterUI e são aceitos os arquivos `.gguf`.

![model_selected](https://github.com/user-attachments/assets/453bc5ae-c496-4968-8578-b0b7cdf74251)

Os modelos podem ser encontrados no repositório de [Bartowski](https://huggingface.co/bartowski), no Hugging Face.

Após isso, fiz um teste executando um prompt simples, veja abaixo os resultados em tela:

![prompt_1](https://github.com/user-attachments/assets/cd331e95-20f1-46ed-b2d9-08e45743954e)
![prompt_2](https://github.com/user-attachments/assets/bee06d35-3d09-4e2c-b019-fa941ed045b0)
![prompt_3](https://github.com/user-attachments/assets/0468ff78-add7-4b18-9413-47068d4f6371)
![prompt_4](https://github.com/user-attachments/assets/8cb97169-349d-4795-b2af-0d3f2ed916fb)

Nesta demonstração, validei a capacidade do modelo **Llama 3.2 3B** de atuar como um engenheiro de dados sênior em um ambiente totalmente offline. O objetivo foi processar uma pipeline de dados completa (ETL) diretamente em um dispositivo móvel.

### O Desafio Técnico
Solicitei ao modelo a criação de um script Python capaz de:
1. Carregar dados de um arquivo Excel (`.xlsx`) via Pandas.
2. Realizar transformações de dados (renomeação de colunas e limpeza).
3. Persistir os dados em um banco de dados **SQLite** local.
4. Executar queries SQL de filtragem para validar a ingestão.

### Performance e Telemetria (Snapdragon 7+ Gen 2)
Os resultados de performance evidenciam a viabilidade de SLMs (Small Language Models) para produtividade técnica:

* **Prompt Processing (16.38 t/s):** O hardware processou o contexto quase instantaneamente, permitindo uma interação sem latência percebida.
* **Text Generation (8.15 t/s):** A velocidade de escrita superou a média de leitura humana, gerando um script complexo em cerca de 85 segundos.
* **Eficiência de Memória:** O uso da quantização **Q4_K_M** permitiu que o modelo operasse dentro da margem de segurança dos 8GB de RAM do Poco F5, mantendo o sistema estável e responsivo.

### Qualidade da Solução Gerada
O modelo não entregou apenas um "código funcional", mas uma solução muito interessante dado fato de ser uma SLM local em um smartphone que nem é um flagship:
* **Modularidade:** Divisão clara entre funções de carga, criação de tabela e filtragem.
* **Resiliência:** Implementação de blocos `try-except` para capturar falhas de IO e banco de dados.
* **Camada Educacional:** Inclusão automática de um *Language Learning Breakdown*, explicando a semântica de cada biblioteca utilizada (Pandas e SQLite3).

### Configuração
Abaixo uma imagem da configuração geral que usei nesse projeto pessoal para melhor otimizar o modelo ao meu hardware disponível.

![sampler](https://github.com/user-attachments/assets/888d4d4b-e867-4047-82e7-236de07c9a3c)

## Conclusão
É um projeto simples, principalmente por causa dos grandes avanços na comunidade, com modelos open-source disponíveis, as melhorias brutais nesses modelos de IA que permitem que smartphones rodem, localmente, de forma totalmente gratuita e com total privacidade, um poderoso recurso de IA para resolução de problemas, tutoria, etc. Com essa experiência, minha mente se abre a possibilidades diversas! Quero depois testar um modelo em meu computador pessoal, penso em como é possível que tenhamos servidores privados para usarem esses modelos, integrados com APIs, levando modelos adaptados às necessidades de possíveis clients e com escopo especializado em tarefas específicas. Também vejo como é interessante pensar em como modelos privados podem ser úteis em projetos de dados sensíveis (teria que estudar mais, mas entendo que haja privacidade num uso interno em hardware próprio) ou em projetos com desejo de maior privacidade de dados, permitindo que esses modelos sejam usados para responder a perguntas de analistas de negócio e outros stakeholders, sendo construídos e mantidos por um time de Ciência de Dados e IA, em que teríamos analistas de dados, engenheiros de dados, cientistas de dados e demais profissionais de dados trabalhando em conjunto para um nível de interação e facilitação final no universo de dados como jamais fora visto em outros tempos.

Isso me estimula a seguir adentrando nessa área incrível que é a Inteligência Artificial. Sei que não sou um especialista, talvez jamais o seja, mas mesmo alguém com um conhecimento de Engenharia de Dados, sem ser um pesquisador em IA ou profundamente conhecedor de regras estatísticas ou matemáticas, conseguiu resolver uma dor pessoal: ter um assistente de IA 100% gratuito, localmente disponível e totalmente privado. Isso não significa que eu vá cancelar minha assinatura de IA na nuvem, mas certamente aumenta meu alcance de usos em contextos de ausência de Internet.

Por fim, pode ser assustador para alguns essa nova "dependência" de IA, mas como alguém profundamente curioso e cheio de ideias, eu enxergo a IA como uma forma de confabular meus pensamentos, tendo um árbitro robótico que é capaz de apontar para detalhes que, dada minha humanidade falha, que se distrai e não é robótica, me permite captar nuances do meu próprio pensar, de modo a otimizar meu pensamento, melhorar a mim mesmo com tutoria e ir direto ao ponto em conteúdos que, doutro modo, eu levaria mais tempo consumindo via outros recursos.

</details>

---

<details>
<summary>🇺🇸 <b>English Version</b></summary>

## Overview
This project demonstrates the implementation of a **100% offline** AI assistant on a mobile device. The goal is to create a tutor specialized in **Data Engineering** and **Polyglot Studies**, optimized for restricted hardware, ensuring privacy and zero costs.

## Details
I really like languages and I really enjoy interacting with AI. Chatbots are helping me a lot with language studies, learning new words (e.g., if I'm reading a book in English, I can ask about words in the given context, learning from the AI's cultural experience to explain in a way that Google Translate alone couldn't, while also functioning as a more interactive dictionary) and programming or consultations (e.g., what is the specific Git command to change from the main branch to another, while creating the branch?).

Although I have a monthly AI subscription for professional, personal, and study purposes, I always thought about how fun it would be to have my own AI on my phone. Talking to Gemini, my tutor, I realized everything was simpler than I imagined! I discovered MLC Chat, but had some issues; to save time, I found the perfect solution with ChatterUI, an open-source project that offers a great interface and allows us to load models directly from Hugging Face!

## Developing the project
The first step was obtaining the ChatterUI APK from the official repository: [ChatterUI](https://github.com/Vali-98/ChatterUI). After installing it on Android, I created a "Character". This allows for personality settings and scoping the model. In my case, I wanted an AI for Data Engineering with Python and SQL, while also assisting my English and Chinese studies (with Portuguese as my native base).

![character_creation](https://github.com/user-attachments/assets/eaa77430-3cff-4d99-9360-e980ea5fbe83)
> Here I provided the prompts to focus the model on my goals.

After the persona setup, I loaded the desired model in the "Models" section of ChatterUI using `.gguf` files.

![model_selected](https://github.com/user-attachments/assets/453bc5ae-c496-4968-8578-b0b7cdf74251)

Models can be found at [Bartowski's](https://huggingface.co/bartowski) Hugging Face repository.

I then tested a simple prompt; results are shown below:

![prompt_1](https://github.com/user-attachments/assets/cd331e95-20f1-46ed-b2d9-08e45743954e)
![prompt_2](https://github.com/user-attachments/assets/bee06d35-3d09-4e2c-b019-fa941ed045b0)
![prompt_3](https://github.com/user-attachments/assets/0468ff78-add7-4b18-9413-47068d4f6371)
![prompt_4](https://github.com/user-attachments/assets/8cb97169-349d-4795-b2af-0d3f2ed916fb)

In this demonstration, I validated the **Llama 3.2 3B** model's ability to act as a senior data engineer offline. The goal was to process a complete ETL pipeline directly on a mobile device.

### The Technical Challenge
I requested a Python script capable of:
1. Loading Excel data (`.xlsx`) via Pandas.
2. Performing data transformations (renaming columns and cleaning).
3. Persisting data into a local **SQLite** database.
4. Executing SQL filter queries to validate ingestion.

### Performance and Telemetry (Snapdragon 7+ Gen 2)
Performance results show the viability of SLMs (Small Language Models) for technical productivity:

* **Prompt Processing (16.38 t/s):** The hardware processed context almost instantly, allowing interaction without perceived latency.
* **Text Generation (8.15 t/s):** Writing speed exceeded human reading average, generating a complex script in about 85 seconds.
* **Memory Efficiency:** Using **Q4_K_M** quantization allowed the model to operate within the safety margin of the Poco F5's 8GB RAM, keeping the system stable.

### Quality of the Generated Solution
The model delivered a professional solution despite being a local SLM on a non-flagship smartphone:
* **Modularity:** Clear division between loading, table creation, and filtering functions.
* **Resilience:** `try-except` blocks to capture IO and database failures.
* **Educational Layer:** Automatic inclusion of a *Language Learning Breakdown*, explaining the semantics of Pandas and SQLite3.

### Configuration
Below is the general configuration used to optimize the model for my hardware.

![sampler](https://github.com/user-attachments/assets/888d4d4b-e867-4047-82e7-236de07c9a3c)

## Conclusion
This is a simple project, made possible by open-source advancements. AI models now allow smartphones to run powerful tools locally, for free and with total privacy. This experience opens my mind to many possibilities, like testing models on my PC or using private servers for sensitive data. 

This stimulates me to dive deeper into AI. I solved a personal pain point: having a 100% free, local, and private AI assistant. It doesn't replace my cloud AI, but it extends my capabilities where there's no internet. 

Finally, I see AI as a way to confabulate my thoughts, having a robotic arbiter that points out details I might miss, optimizing my thinking and learning process.

</details>

---

<details>
<summary>🇨🇳 <b>中文版</b></summary>

## 项目概况
该项目展示了在移动设备上实现 **100% 离线** AI 助手。目标是创建一个专注于 **数据工程** 和 **多语言学习** 的专业导师，并针对资源受限的硬件进行了优化，确保完全的隐私和零成本。

## 详细内容
我非常喜欢语言，也非常喜欢与 AI 互动。聊天机器人对我的语言学习很有帮助，比如学习新词（例如，如果我在读一本英文书，我可以询问特定语境下的词汇，从 AI 的文化经验中学习，这种解释方式是仅使用谷歌翻译无法做到的，此外它还能作为一个更具互动性的词典），以及编程咨询（例如，Git 中从 main 分支切换到另一个分支并同时创建该分支的命令是什么？）。

虽然我为了工作和学习订阅了月的 AI 服务，但我一直在想，如果手机里有自己的 AI 该多有趣。在与我的导师 Gemini 交流后，我发现这一切比我想象的要简单！我发现了 ChatterUI，这是一个开源项目，提供出色的界面并允许直接从 Hugging Face 加载模型。

## 项目开发
第一步是获取 ChatterUI 的 APK。官方仓库链接：[ChatterUI](https://github.com/Vali-98/ChatterUI)。在 Android 上安装后，我创建了一个“角色”（Character）。这允许设置性格和模型范围。在我的案例中，我需要一个能用于 Python 和 SQL 数据工程的 AI，同时辅助我的英语和中文学习。

![character_creation](https://github.com/user-attachments/assets/eaa77430-3cff-4d99-9360-e980ea5fbe83)
> 在这里，我输入了提示词，使模型专注于我的目标。

完成角色设置后，我在 ChatterUI 的“Models”部分加载了 `.gguf` 格式的模型。

![model_selected](https://github.com/user-attachments/assets/453bc5ae-c496-4968-8578-b0b7cdf74251)

可以在 Hugging Face 的 [Bartowski](https://huggingface.co/bartowski) 仓库中找到这些模型。

随后我测试了一个简单的提示词，结果如下：

![prompt_1](https://github.com/user-attachments/assets/cd331e95-20f1-46ed-b2d9-08e45743954e)
![prompt_2](https://github.com/user-attachments/assets/bee06d35-3d09-4e2c-b019-fa941ed045b0)
![prompt_3](https://github.com/user-attachments/assets/0468ff78-add7-4b18-9413-47068d4f6371)
![prompt_4](https://github.com/user-attachments/assets/8cb97169-349d-4795-b2af-0d3f2ed916fb)

在此演示中，我验证了 **Llama 3.2 3B** 模型在离线环境下充当高级数据工程师的能力。目标是在移动设备上直接处理完整的 ETL 数据流水线。

### 技术挑战
我要求模型创建一个 Python 脚本，能够：
1. 通过 Pandas 加载 Excel 文件 (`.xlsx`)。
2. 进行数据转换（重命名列和清洗）。
3. 将数据持久化到本地 **SQLite** 数据库。
4. 执行 SQL 过滤查询以验证数据入库。

### 性能与遥测 (骁龙 7+ Gen 2)
性能结果证明了 SLM（小语言模型）在技术生产力方面的可行性：

* **提示词处理 (16.38 t/s):** 硬件几乎瞬间处理了上下文，交互无延迟感。
* **文本生成 (8.15 t/s):** 写入速度超过了人类阅读平均水平，约 85 秒内生成了复杂的脚本。
* **内存效率:** 使用 **Q4_K_M** 量化使模型能够在 Poco F5 的 8GB RAM 安全范围内运行，保持系统稳定。

### 生成方案的质量
尽管是在非旗舰智能手机上的本地 SLM，该模型仍提供了专业的方案：
* **模块化:** 加载、建表和过滤功能划分清晰。
* **弹性:** 实现 `try-except` 块以捕获 IO 和数据库错误。
* **教育层:** 自动包含“语言学习分析”，解释了 Pandas 和 SQLite3 库的语义。

### 配置
以下是用于优化模型以适配硬件的常规配置图像。

![sampler](https://github.com/user-attachments/assets/888d4d4b-e867-4047-82e7-236de07c9a3c)

## 结论
这是一个简单的项目，得益于开源社区的进步。AI 模型现在允许智能手机本地运行强大的工具，且完全免费和隐私。这次经历拓宽了我的思路，例如在 PC 上测试模型或在敏感数据项目中使用私有服务器。

这激励我进一步探索 AI 领域。我解决了一个个人痛点：拥有一个 100% 免费、本地且私密的 AI 助手。它不会取代我的云端 AI，但在无网络环境下扩展了我的能力。

最后，我将 AI 视为一种完善思维的方式，它像是一个机器人裁判，能指出我可能忽略的细节，优化我的思考和学习过程。

</details>

---
