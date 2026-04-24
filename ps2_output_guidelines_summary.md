# Problem Statement 2 (PS-2) Output Guidelines Summary

Based on the official documents in `/ps-2/PS2_Output_Guidelines/`, here is a comprehensive breakdown of what is expected for your outputs. 

For **every claim**, participants must generate **two distinct outputs**:

## 1. Structured Output (Row-wise / Excel Format)
You are required to extract objective data into a strictly structured format. The exact columns vary slightly depending on the procedure, but generally follow this 7-section structure:

* **SECTION 1: Claim Details** 
  * Unique Claim ID linking to the image/case.
* **SECTION 2: Image Classification** 
  * Classify the type of radiological image submitted at pre-procedure and/or post-procedure stages (e.g., "Cardiac angiogram", "USG Abdomen", "Chest X-ray", "Absent").
* **SECTION 3: Image Description (Objective)**
  * **Strictly describe what is seen, not what it means.**
  * *MC011A (PTCA)*: Coronary Anatomy (LMCA, LAD, LCX, RCA prox/mid/distal).
  * *MG029A (COPD)*: Lung fields, Costophrenic angles, Hilum, Midline shift, Cardiac size.
  * *SG039C (Cholecystectomy)*: Liver, Gallbladder (stones), Spleen, Kidneys, Bladder, Peritoneal/Pericholecystic fluid.
  * *SU007A (PCNL)*: Pelvicalyceal system, Ureter, Urinary bladder, Stone visualization, Stent/PCN tube.
* **SECTION 4: Report Validity and Correlation**
  * **Intra-Report Consistency:** Does the written report's observation match its own impression? (*Consistent / Partially supported / Unsupported*)
  * **Inter-Report Correlation:** Do the visual image features support what the written report claims?
* **SECTION 5: Claim, Package & STG Alignment**
  * Check if both pre- and post-procedure investigations align with the Standard Treatment Guidelines (STG).
  * Provide reasoning mapped to PPD/CPD logic.
* **SECTION 6: Stage & Timeline Awareness**
  * Extract dates: Admission, Pre-procedure, Post-procedure, Discharge.
  * **Flags:** Flag if pre-procedure documents are >1 month old, or if post-procedure documents fall outside the admission-discharge window.
* **SECTION 7: Quality**
  * Comment on image usability (e.g., "Good enough for human eyes", "Poor quality", "Artefacts present").

---

## 2. Textual Summary (PDF format)
A short, human-readable case summary that consolidates all the structured outputs into a note suitable for PPD/CPD (Processing/Claim Processing Doctor) review.
* **Expected Content**: Key image description, validity outcome, STG alignment statement, and timeline/flags summary.
* **Tone**: Assistive, neutral, non-diagnostic.

---

## 🚨 CRITICAL RULES FOR PARTICIPANTS 🚨
If you are generating these outputs via an AI model or script, you must adhere strictly to these constraints:
1. **Use observational language only.**
2. **DO NOT confirm diagnoses** (e.g., do not evaluate CAD severity, pneumonia, etc. - just state what is visually present).
3. **DO NOT recommend approval or rejection** of the claim.
4. **Explicitly mention uncertainty** if the image quality is poor.
5. **All fields must be populated** (use terms like *"Not assessed"* or *"Not seen"* if data is missing).
6. Provide specific required imaging depending on the package (e.g., PCNL *requires* pre-op IVP and post-op X-ray KUB; COPD *only* requires post-op imaging).
