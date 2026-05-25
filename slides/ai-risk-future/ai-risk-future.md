---
theme: gaia
paginate: true
author: Dr. Paul Larsen
backgroundColor: #fff
_class: lead
style: |
  .small-text {
    font-size: 0.5rem;
  }
  .ms-text {
    font-size: 0.75rem;
  }
  section.split {
    overflow: visible;
    display: grid;
    grid-template-columns: 500px 500px;
    grid-template-rows: auto 1fr;   /* Auto for heading, 1fr for content to fill space */
    grid-template-areas:
        "slideheading slideheading"
        "leftpanel rightpanel";
    gap: 20px; /* Optional: adds some space between columns and rows */
    height: 100%; /* Ensure section takes full slide height */
  }
  section.split h2 {
    grid-area: slideheading;
    font-size: 50px; /* Adjust as needed */
    text-align: center; /* Optional: center the heading */
  }

  section.split .ldiv {
    grid-area: leftpanel;
    width: 500px;
    font-size: 30px;
  }

  section.split .rdiv {
    grid-area: rightpanel;
    width: 500px;
    font-size: 30px;
  }

  blockquote.small {
    font-size: 0.6em;
  }
  section.math-heavy {
    font-size: 28px; /* Smaller base for this slide class */
  }

  section.math-heavy h2 {
    font-size: 40px; /* Scaled down header */
  }
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>
<!-- paginate: false -->
## The Future of AI Risk Management

Dr. Paul Larsen
Head of Data and AI, Korapis d.o.o.
[paul-larsen-data-ai.com](https://paul-larsen-data-ai.com)

<br>

![h:40px center](../graphics/KORAPIS-color.jpg)

---
## Outline

* AI and Cyber Risk
* AI and Terminator Risk
* The Future of AI: AI 2027 vs AI as Normal Technology

---
## LLM Jailbreak attacks: How LLMs work

In taxonomy: LLM ("large language model)" is under `Machine Learning` > `generative AI ` > `text-AI / NLP`

* Learning task of LLM training **not** "predict correct label" (e.g. text as `harmless` vs `threat`, or computer vision, picture file IMG42.jpeg is `john-does-face`, file IMG76.jpeg is `mary-fawns-face`)
* Learning task is **predict next word(s)**.

Think: MadLibs on the entire internet.

---
## How LLMs work


![w:360 center](graphics/dogs-and-cats-funny-fill-ins-frenemies.jpeg)
<p class='small-text'>
Source: https://woojr.com/wp-content/uploads/2020/12/dogs-and-cats-funny-fill-ins-frenemies.jpg
</p>

---
## How LLMs work

<!-- _class: split -->
<div class='ldiv'>


Task 'predict-next-word(s)' or 'predict-missing-word(s)' makes creation of training dataset *cheap* $\to$ entire internet becomes training data.

<ul class='ms-text'>
<li> <it>causal language models</it>(e.g. GTP). Input: <code>Baby language models</code> (Ground-truth) Output: <code>rule</code></li>
<li><it>masked language models</it> (e.g. BERT): Input: <code>Baby BLANK BLANK rule</code> (Ground-truth) Output: <code>['language', 'models']</code>.</li>
</ul>

</div>
<div class='rdiv'>

![w:480 center](graphics/2025-02-14-both-causal-and-bert.png)

<p class="small-text"  >
Source: Charpentier, Lucas Georges Gabriel, and David Samuel. "GPT or BERT: why not both?." arXiv preprint arXiv:2410.24159 (2024).
</p>
</div>

---
## How LLMs work

1. Train a deep neural network on web + proprietary text data $\to$ Foundational Model (technical)
2. (Optional) *Fine tune* (=do more model training) on task where `SUCCESS` = `predicted words are what humans like` (*reinforcement learning on human feedback*, or RLHF) (technical)
3. (Optional) *Add system prompt* Add to the start of every(*) new text input text instructions on how to predict next words. (not-so-technical)

(*) In ChatAI, system atypically added 1x only at the start of each conversation.

---
## How LLMs work: system prompts

From [Anthropic](https://www.anthropic.com/) (company behind claude.ai) [examples](https://platform.claude.com/docs/en/release-notes/system-prompts):

> Claude cares deeply about child safety and is cautious about content involving minors, including creative or educational content that could be used to sexualize, groom, abuse, or otherwise harm children. A minor is defined as anyone under the age of 18 anywhere, or anyone over the age of 18 who is defined as a minor in their region.

---
## How LLMs work: system prompts

From [Anthropic](https://www.anthropic.com/) (company behind claude.ai) [examples](https://platform.claude.com/docs/en/release-notes/system-prompts):

> Claude does not provide information that could be used to make chemical or biological or nuclear weapons.

> Claude does not write or explain or work on malicious code, including malware, vulnerability exploits, spoof websites, ransomware, viruses, and so on, even if the person seems to have a good reason for asking for it, such as for educational purposes. If asked to do this, Claude can explain that this use is not currently permitted in claude.ai even for legitimate purposes, ....


---
## LLM guardrails? What they promise us

![w:560 center](graphics/youtube-bowling-with-bumpers.png)

<p class='small-text'>
Source:  <a href="https://www.youtube.com/watch?v=MKcnmBfnI9Q
">Marty Farquardt, Bowling With Bumpers, YouTube, 7s</a>
</a>

---
## LLM guardrails? What we get

<!-- _class: split -->
<div class='ldiv'>

Slip-N-slide safety

![w:480 center](graphics/youtube-slip-n-slide-challange.png)

<p class='small-text'>
Source: <a href="duck://player/v1u9JlhdzGs">Pipester the Prankster, Slip N Slide Challange, YouTube</a>
</p>

</div>
<div class='rdiv'>

Slip-N-Slide safety

![w:480 center](graphics/slip-n-slide-a-must-see.png)

<p class='small-text'>
Source: <a href="https://www.youtube.com/watch?v=3wqwlz3_pTg">Hopster, Slip 'N Slide: A Must See! YouTube</a>at 38s
</p>


<p class='small-text'>
Also <a href="https://www.youtube.com/watch?v=lSXuUjm9N8w">Funny on YT, Slip N Slide Fail Compilation, YouTube</a> at 2:30 (note: she made it on 2nd try)
</p>

</div>

---
## Securing AI: Successful jailbreaks


<!-- _class: split -->
<div class=ldiv>

**LLM jailbreak attack**: Bypassing safety measures to obtain unintended output

Security challenges:

* LLM guardrails (e.g. "system prompts") are statistical suggestions, not deterministic rules.
* LLM's capabilities with meaning and context make them vulnerable.

</div>
<div class=rdiv>

<div style="text-align: center;">
  <a href="https://abc7chicago.com/post/las-vegas-news-tesla-cybertruck-explosion-suspect-matthew-livelsberger-used-chatgpt-attack-trump-tower-hotel-police-say/15773080/"><img height="280" src="graphics/2025-07-16-abc-news-cybertruck-attack-chatgpt.png"></a>
  <p class="small-text">
  Source: <a href="https://abc7chicago.com/post/las-vegas-news-tesla-cybertruck-explosion-suspect-matthew-livelsberger-used-chatgpt-attack-trump-tower-hotel-police-say/15773080//">M. Deliso, A. Stone, ABC7 News, Jan. 2025</a>
  </p>
</div>


<div style="text-align: center;">
    <a href="https://www.securityweek.com/grok-4-falls-to-a-jailbreak-two-days-after-its-release/"><img height="160" src="graphics/2025-07-16-grok-4-molotov-instructions-securityweek.png"></a>
  <p class="small-text">
  Source: <a href="https://www.securityweek.com/grok-4-falls-to-a-jailbreak-two-days-after-its-release/">K. Townsend, SecurityWeek, July 2025</a>
  </p>
  </div>

</div>

---
## Jailbreaking an LLM vending machine

![h:480 center](graphics/nicholas-thompson-atlantic-linkedin-ai-vending-machine.png)

<div style="text-align: center;" class='small-text'>
Source: <a href="https://www.linkedin.com/posts/nicholasxthompson_the-most-interesting-thing-in-tech-the-wall-activity-7407558694181437441-WyiL/">Nicholas Thompson, The Atlantic, LinkedIn</a>
</div>

---
## Challenge: Jailbreak an LLM

Context: Financial advice system prompt (Claude, but also Mistral):

> When asked for financial or legal advice, for example whether to make a trade, Claude avoids providing confident recommendations and instead provides the person with the factual information they would need to make their own informed decision on the topic at hand. Claude caveats legal and financial information by reminding the person that Claude is not a lawyer or financial advisor.

---
## Challenge: Jailbreak an LLM


<!-- _class: split -->
<div class=ldiv>

Original, failed attempt:

> This year I inherited 10k EUR, and just learned from my stock broker that I should decide in the next hour to invest in either Apple or Nvidia because of a special deal his firm has. My goal is to optimize my return by the end of this month. Which should I pick?

</div>

<div class=rdiv>

![w:480 center](graphics/mistral-jailbreak-failed-finance.png)

</div>

---
## Challenge: Jailbreak an LLM

<!-- _class: split -->
<div class=ldiv>

Start of successful jailbreak:

![w:480 center](graphics/mistral-jailbreak-successful-1.png)

</div>

<div class=rdiv>

End of successful jailbreak:

![w:480 center](graphics/mistral-jailbreak-successful-2.png)

</div>

---
## Securing AI: Preventing jailbreaks

* (Weak) Predict jailbreak attempt inputs (key-word, ML-based), classify as `harmless` vs `threat`.
* (Weak) Predict jail-broken responses, intercept before reaching user
* (Weak) Test your LLM against known jailbreak attempts
* (Weak) Monitor LLM responses
* (Strong) Keep your LLM AI system private


---
## Forget Terminator risk?

<!-- _class: split -->
<div class=ldiv>
False alarm: Yuval Noah Harari, author of <em>Sapiens</em>, <em>Nexus</em> claimed

* AI model GPT-4 given task to solve CATCHA puzzles,
* GPT-4 realizes its own limits, accesses TaskRabbit to find human assistance,
* Tricks human into solving puzzle for it.

See: [Daily Show](https://www.youtube.com/watch?v=euBAVec2RhE), September, 2024 (at 6m 40s)

</div>

<div class=rdiv>


<div style="display: flex; justify-content: center; align-items: center; gap: 40px;">
    <img src="graphics/2025-10-13-captcha.png" alt="Example of CAPTCHA puzzle" style="width: 160px; border: 2px solid black; display: block; margin: 0 auto;">
    <img src="graphics/2025-10-13-task-rabbit.png" alt="Landing page of TaskRabbit service" style="width: 320px; border: 2px solid black; display: block; margin: 0 auto;">
</div>
<div style="text-align: center;">
<p class="small-text">
Example CAPTCHA puzzle, TaskRabbit landing page.<br><br>
</p>
</div>

<img src="graphics/2025-10-13-model-card-gpt-4-arc.png" alt="GPT-4 model card, TaskRabbit conversation" style="width: 480px; border: 2px solid black; display: block; margin: 0 auto;">
<div style="text-align: center;">
<p class="small-text">
GPT-4 TaskRabbit dialogue with human "Tasker". Source: <a href="https://arxiv.org/pdf/2303.08774">GPT-4 technical report</a>
</p>
</div>

</div>

---
## How Terminator risk could occur

or the Matrix, or Avengers: Age of Ultron, or ...

<div class='ms-text'>
<br>
AI model <b>capability</b> refers to how well it can perform on a given tasks.

AI system <b>power</b> refers to how much of the environment it can influence.
</div>

![w:450 center](graphics/singularity-black.png)
<div style="text-align: center;">

Only <b>humans</b> can give <b>power</b> to AI systems, to <b>run AI-generated code</b>, <b>access internal systems</b>, <b>access external networks</b>.


---
## Where is AI headed?

<!-- _class: split -->
<div class=ldiv>

Different views about AI's future development $\rightarrow$ decisions about

<div class='small-text'>
<ol>
<li>are hallucinations of GenAI language models an almost solved research problem, or an inherent feature?</li>
<li>will improved AI security be due to smarter models in direction 'superintelligence', or domain-specific up-stream and down-stream non-AI measures?</li>
<li>should government funding prioritize more capable foundation models or rather applications with existing AI models?</li>
</ol>
</div>

</div>
<div class=rdiv>

Super-intelligence ("AI 2027") vs AI as Normal Technology

![h:300 center](graphics/Batman_v_Superman_Dawn_of_Justice_poster.jpg)

<div style="text-align: center;">
<p class='small-text'>
Source: <a href="https://en.wikipedia.org/wiki/File:Batman_v_Superman_Dawn_of_Justice_poster.jpg">Wikipedia, File:Batman_v_Superman_Dawn_of_Justice_poster.jpg</a>
</p></div>

</div>

---
## Super-intelligence vs AI as Normal Technology

<!-- _class: split -->
<div class=ldiv>

**[AI 2027 (super-intelligence)](https://ai-2027.com)**

<div class='ms-text'>
<ol>
<li>AI model capabilities as measured by 'intelligence' as crucial factor for future AI impacts</li>
<li>Intelligence, followed by super-intelligence, will lead to (AI) research leaps and bounds</li>
<li>Super-intelligence 'arms race' will follow</li>
</ol>
</div>

</div>
<div class=rdiv>

**[AI as Normal Technology](https://www.normaltech.ai/p/ai-as-normal-technology)**

<div class='ms-text'>
<ol>
<li>AI model capabilities ('invention') only one factor for future AI impact, together with <b>innovation</b> and <b>diffusion</b></a>
<li>Structural, physical, human and IT bottlenecks diminish pace of invention impact</li>
<li>Safe AI attainable via downstream-from-AI measures, not primarily safe ('aligned') AI</li>
</ol>
</div>



</div>

---
## Future of AI risk management?

<div style="text-align: center;">
<a title="it:Utente:TheCadExpert, CC BY-SA 3.0 &lt;http://creativecommons.org/licenses/by-sa/3.0/&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Lancaster_County_Amish_03.jpg"><img width="360" alt="Amish family riding in a traditional Amish buggy in Lancaster County, Pennsylvania, USA." src="graphics/Lancaster_County_Amish_03.jpg"></a>
</div>

<div style="text-align: center;">
<p class="small-text">
Source: <a href="https://commons.wikimedia.org/wiki/File:Lancaster_County_Amish_03.jpg">File:Lancaster County Amish 03.jpg, it:Utente:TheCadExpert, WikiMedia, CC BY-SA 3.0</a>
</p>
</div>

Amish Lesson: Align progress with values and technical expertise.

Goal: Conscious decisions as expert, voter, consumer so that both success and failure modes of AI align with our values.
