# Report — Dorm Decor Inquiry Responder

## Business Use Case
This prototype automates the first response to customer inquiries for a small dorm interior decorating business. When a potential customer sends a message describing their style preferences, budget, and needs, the system drafts a warm, professional reply email on behalf of the business owner. This saves time during busy move-in seasons and ensures no inquiry goes unanswered.

## Model Choice
I used Claude (claude-opus-4-5) via the Anthropic API. I chose this model because it produced natural, conversational email responses that felt genuinely warm rather than robotic. The model handled vague and specific inquiries equally well and required minimal prompting to stay on task.

## Baseline vs. Final Design
The initial prompt produced good responses but included excessive emojis and bold text that felt unprofessional for a real business email. In the second revision I removed emojis and bold text and changed the tone instruction from "friendly" to "professional," which produced cleaner output. In the third revision I added a line encouraging customers to book soon due to move-in season filling up fast. This added a subtle but realistic sense of urgency that made the responses feel more like something a real business would send.

## Where the Prototype Still Fails
The system struggles with very vague inquiries — it sometimes makes assumptions about style or budget instead of asking clarifying questions. It also cannot handle follow-up questions or multi-turn conversations. Any response should be reviewed by the business owner before sending, especially for unusual or sensitive requests.

## Deployment Recommendation
I would recommend deploying this as a draft assistant only — meaning the system generates a first draft that the owner reviews and edits before sending. It should not be set up to send emails automatically. With human review in the loop, this tool could meaningfully reduce the time spent on repetitive inquiry responses during peak season.
