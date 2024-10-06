### **ElderGuard Video Recording Script**:

#### **1. Introduction**
**Speaker:**
“Hello, we’re Team Karasuno, and we’re excited to present our project, **ElderGuard**.”

**Speaker:**
“Falls among the elderly are a significant health concern, especially in care facilities. Every year, millions of older adults suffer serious injuries from falls. Our goal with ElderGuard is to provide a **real-time monitoring system** that helps caregivers detect and respond to these incidents as quickly as possible.”

#### **2. Problem Statement**
**Speaker:**
“The problem we’re addressing is the lack of real-time fall detection in elderly care. Caregivers might not always notice when someone has fallen or is lying down in a vulnerable position, especially in large care homes or nursing facilities.”

**Speaker:**
“ElderGuard tackles this problem by providing a real-time monitoring system that uses pose detection to identify when a person has been lying down for too long and alert caregivers through **visual and auditory cues**.”

#### **3. Solution Overview**
**Speaker:**
“Let’s take a quick look at how ElderGuard works.”

[**Screen Recording of System**]

**Speaker:**
“Here’s the main interface of ElderGuard. The system is designed to be simple and intuitive for caregivers or monitoring staff. The key features include:”
- **Real-time video feed**: A live video feed is displayed, which monitors the room.
- **Pose detection**: ElderGuard analyzes the video feed to detect when a person is lying down and triggers an alert if they stay in that position for more than a set threshold.
- **Sound alerts**: When a person is detected lying down for too long, the system plays an alert sound to notify caregivers.
- **Event logging**: The system also logs each detection event, showing timestamps of when a person was lying down and when they were reset.”

#### **4. Demo**
[**Switch to a live demo of ElderGuard**]

**Speaker (while demoing):**
“Now, let’s see ElderGuard in action. In this example, we have a person lying down. You’ll notice that after a few seconds, ElderGuard detects that they are lying down for more than the configured threshold and triggers a **sound alert**.”

[**Allow the alert sound to play**]

**Speaker:**
“The person’s status also turns red in the table, signaling to the caregiver that action is needed. The event is logged in the log panel below, showing when the detection happened.”

**Speaker:**
“To reset the system, the caregiver can press the **Reset** button, which stops the alert and updates the person’s status back to ‘Not lying down.’ The log is also updated with the reset event.”

#### **5. Technology Stack**
**Speaker:**
“To build ElderGuard, we used a range of tools and technologies. Our main framework is **Flask**, which handles the web application and serves the user interface. We used **OpenCV** and **MediaPipe** to implement the pose detection system that monitors for lying down behaviors.”

**Speaker:**
“The system processes live video streams, detects when someone is lying down, and triggers both sound alerts and logs events in real-time, all within a simple, easy-to-use interface.”

#### **6. Conclusion & Impact**
**Speaker:**
“In conclusion, **ElderGuard** provides a simple yet effective solution for monitoring elderly individuals in care facilities. By detecting when someone is lying down for too long, we hope to reduce the risk of serious injuries due to falls.”

**Speaker:**
“This system can be deployed in nursing homes, hospitals, or even private homes to improve care and provide peace of mind to caregivers. Thank you for watching our demo of ElderGuard!”

[**End Screen**]: 
“Thank you from Team Karasuno.”
