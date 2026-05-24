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

---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>
<!-- paginate: false -->
## AI Risk Management

### Why it's different, why it's important

Dr. Paul Larsen
Head of Data and AI, Korapis d.o.o.
[paul-larsen-data-ai.com](https://paul-larsen-data-ai.com)

<br>

![h:40px center](../graphics/KORAPIS-color.jpg)


---
<!-- paginate: true -->
## Risk and Regulation

Historical pattern: exuberance $\to$ crisis $\to$ regulation

![h:300 center](graphics/exuberance-crisis-regulation.png)


---
## A brief history of financial disaster

![h:300 center](graphics/history-financial-disaster.png)

---
## What is risk regulation?

<!-- _class: split -->
<div class=ldiv>

The risk of losing (money) due to

* Credit: counter-party default
* Market: market movements
* Operational: something going wrong that shouldn't
* Liquidity: funding mismatches
* Insurance: unexpected loss of premium or increase of claims

</div>
<div class=rdiv>

$\ldots$ and the regulation that results from disasters big and small
* [Basil Framework (banking)](https://www.bis.org/basel_framework/),
* [Solvency II (insurance)](https://www.eiopa.europa.eu/browse/solvency-2_en)
* [The AI Act (EU)](https://www.europarl.europa.eu/doceo/document/TA-9-2024-0138_EN.html)

</div>

---
## Where is the AI crisis?

---
## AI risk is different

1. AI failure modes differ from human and non-AI software

![h:300 center](graphics/human-ai-software-black.png)

<div style="text-align: center;">
<p class="ms-text">
How does AI differ from human intelligence and non-AI software?
</p>
</div>

---
## AI risk management is important

2. Banking risk management is well prepared for AI

<div style="display: flex; justify-content: center; align-items: flex-start; gap: 20px;">
    <img src="graphics/cheer-black.png" alt="Cheer image" style="width: 240px;">
    <img src="graphics/ref-black.png" alt="Referee image" style="width: 200px; margin-top: 40px;">
    <img src="graphics/security-black.png" alt="Security image" style="width: 360px;">
</div>

<div style="text-align: center;">
<p class="ms-text">
AI cheerleader (business), referee (risk management) and bouncer (legal, compliance)
</p>
</div>

---

## What makes AI risk management different?

Answer: Experience with failure modes

* About 200.000 years for humans
* About 10-20 years for AI systems

<div style="text-align: center;">
<a title="GuillaumeG, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Omo_Kibish_-_MCN_4152_(cropped).jpg"><img width="200" alt="Omo Kibish - MCN 4152 (cropped)" src="graphics/Omo_Kibish_-_MCN_4152_(cropped).jpeg"></a>
</div>

<div style="text-align: center;">
<p class="small-text">
Source: <a href="https://commons.wikimedia.org/wiki/File:Omo_Kibish_-_MCN_4152_(cropped).jpg">File: Omo Kibish - MCN 4152 (cropped).jpg</a>.
Accessed 2 June. 2025.
</p>
</div>

---
## Implications

If AI system risk management is novel, then need

1. New regulation
1. New risk managers to implement regulation
1. New literature / trainings to guide implementation
1. New IT to support all of above

New regulation: EU's AI Act, Brazil's AI Bill, Australian + S. Korean laws on deep-fakes (all 2024)

---
## Are AI system failure modes truly different?

1. If AI systems are "intelligent", can't we use lessons from human intelligence failure modes?
1. Since AI systems are essentially software automation, aren't IT risk management practices enough?

![h:300 center](graphics/human-ai-software-black.png)

---
## Human vs artificial: computer vision

<!-- _class: split -->
<div class=ldiv>

#### Human driver failures

95% of fatal crashes caused<sup>1</sup>  by human factors
  * alcohol (25%)
  * speeding (30%)
  * inattention (25%)

<p class="small-text">
Source:
<a href=https://road-safety.transport.ec.europa.eu/document/download/a7428369-8eaf-4032-806e-ea08b46028c0_en?filename=ERSO-TR-MainCauses.pdf>EU Commission, Thematic Report: Main factors causing fatal crashes, 15 April 2024</a>
</p>
<p class="small-text">
(1) As a contributory factor.
</p>

</div>

<div class=rdiv>

#### AI driver failures

<img src="graphics/2025-02-19-white-hat-tesla-hack.png" style="width: 500px; border: 2px solid black; display: block; margin: 0 auto;">


<p class="small-text">
Source: <a href=https://www.cnbc.com/2019/04/03/chinese-hackers-tricked-teslas-autopilot-into-switching-lanes.html>Huddleston, Tom, Jr, CNBC, 3 Apr. 2019. Accessed 19 Feb. 2025</a>
</p>

<img src="graphics/2025-06-03-adversarial-stop-stickers.png" style="width: 125px; border: 2px solid black; display: block; margin: 0 auto;">


<p class="small-text">
Source: <a href=https://openaccess.thecvf.com/content_cvpr_2018/papers/Eykholt_Robust_Physical-World_Attacks_CVPR_2018_paper.pdf>Eykholt, Kevin, et al. "Robust physical-world attacks on deep learning visual classification." IEEE conference on computer vision and pattern recognition. 2018</a>
</p>

</div>


---
## Human vs artificial: natural language

<!-- _class: split -->
<div class=ldiv>

#### Human language failures

* spelling error
* grammatical errors
* ignoring or misunderstanding instructions

</div>

<div class=rdiv>

#### AI language failures

* SotA AI: [How many "r"s in "strawberry"? Two.](https://www.inc.com/kit-eaton/how-many-rs-in-strawberry-this-ai-cant-tell-you.html)

<img src="graphics/2025-06-03-rs-in-strawberry-from-2025-12.png" style="width: 175px; border: 2px solid black; display: block; margin: 0 auto;">



* Language embedding failure: Only 10% retrieval success on sentences from EU AI Act (own demo)

</div>

---
## AI systems vs non-AI software

Main ingredients of AI systems

<ol class="ms-text">
<li><b>Historical data</b> relevant to business domain</li>
<li><b>Optimization algorithms</b> to find best parameters from data</li>
<li><b>Human decisions</b> about data selection, algorithms, "best," ...</li>
</ol>

![h:300 center](graphics/data-opt-human-to-ai-black.png)

---
## AI vs non-AI software failure modes

<!-- _class: split -->
<div class=ldiv>

#### Failure: training data bias
<br>
<img src="graphics/facial_bias.png" style="width: 450px; border: 2px solid black; display: block; margin: 0 auto;">

<p class='small-text'>
Source: <a href=https://www.nytimes.com/2018/02/09/technology/facial-recognition-race-artificial-intelligence.html>Steve Lohr, NY Times, 2 Feb. 2018</a>
</p>
</div>

<div class=rdiv>

#### Failure: a prompt is a suggestion, not a rule
<br>
<img src="graphics/2025-06-03-gemini-2024-11-20-please-die.png" style="width: 450px; border: 2px solid black; display: block; margin: 0 auto;">


<p class='small-text'>
Source: <a href=https://www.cbsnews.com/news/google-ai-chatbot-threatening-message-human-please-die/>Alex Clark,  Melissa Mahtani, CBS News, 20 Nov. 2024 </a>
</p>

</div>

---
## AI risk management is different ...

... but risk management principles and practices still apply.

* Identification
* Analysis / evaluation
* Treatment (accept, mitigate, avoid)
* Monitoring and review
* Reporting

---
## Why risk management and AI fit well

<div style="display: flex; justify-content: center; align-items: flex-start; gap: 20px;">
    <img src="graphics/cheer-black.png" alt="Cheer image" style="width: 220px;">
    <img src="graphics/ref-black.png" alt="Referee image" style="width: 190px; margin-top: 35px;">
    <img src="graphics/security-black.png" alt="Security image" style="width: 340px;">
</div>
<div style="text-align: center;">
<p class="small-text">
AI cheerleader (business), referee (risk management) and bouncer (legal, compliance)
</p>
</div>

* Manage risk based on risk and return
* AI: Error budget $\leftrightarrow$ Risk Management: risk appetite

---
## Risk and return with AI: Air Canada

Air Canada AI Chatbot incident:

<div  class="ms-text">
<ul><li>Passenger gets bad advice from Air Canada AI chatbot, misses discount</li>
<li>Air Canada claims correct information was on website, not responsible for chatbot</li>
<li>Tribunal decides for passenger; Air Canada liable, must pay damages</li>
</ul>
</div>

<img src="graphics/2025-10-13-computerworld-air-canada-2024-02-20.png"
  style="width: 450px; border: 2px solid black; display: block; margin: 0 auto;">

<div style="text-align: center;">
<p class="small-text">
Source: <a href="https://www.computerworld.com/article/1612087/air-canada-chatbot-error-underscores-ais-enterprise-liability-danger.html">Grant Gross, ComputerWorld, 24 Feb. 2024</a>
</p>
</div>

---
## Risk and return with AI: Air Canada

Risk and return, applied to Air Canada incident:


* Materialized risk: ~812,02 Canadian dollars (CAD) in damages
* Estimated return figures: Minimum annual wage in Canada: ~30k CAD
* Scenario: ~35 comparable AI incidents same cost as 1 full-time-equivalent

---
## The financial service industry is well-positioned

1. Existing data quality and integrity requirements (e.g. BCBS 239)
2. Experience with model risk, validation

but ...

1. Reporting, actuarial, risk modeling vs AI data work different $\to$ automated data quality + monitoring, e.g. [data contracts](https://paul-larsen-data-ai.com/data-contracts/)
2. Capital and actuarial models share similarities, but many differences to AI models

---
## Workshop outline

1. ~~Introduction~~
2. Managing high-risk AI
2. Managing high-risk AI, II
2. Future of AI risk management

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
