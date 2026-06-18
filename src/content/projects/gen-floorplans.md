---
title: "Generative Floor Plans"
order: 1
role: "Product Management, Design & Leadership"
timeline: "2022 - 2026"
impact: "Almost 4-year evolution of computer vision technology to deliver editable, generative floor plans instantly with every 3D spatial capture"
thumbnail: "/images/projects/gen-floorplans/cover.jpg"
hero: ""
hisImage: ""
videos: ["https://vimeo.com/1202601900", "https://vimeo.com/1202298677", "https://vimeo.com/1202229297"]
media: [{"src": "/images/projects/gen-floorplans/Floorplan 1.jpg", "alt": "Before I started"}, {"src": "/images/projects/gen-floorplans/Floorplan 2.jpg", "alt": "RoomPlan API Launch"}, {"src": "/images/projects/gen-floorplans/Floorplan 3.jpg", "alt": "Early floor plan designs"}, {"src": "/images/projects/gen-floorplans/Floorplan 4.jpg", "alt": "Computer Vision Explorations"}, {"src": "/images/projects/gen-floorplans/Floorplan 5.jpg", "alt": "Advanced Floor Plans"}, {"src": "/images/projects/gen-floorplans/Floorplan 6.jpg", "alt": "SaaS cross platform approach"}, {"src": "/images/projects/gen-floorplans/Floorplan 7.jpg", "alt": "Customizable color themes"}, {"src": "/images/projects/gen-floorplans/Floorplan 8.jpg", "alt": "Feature tracker"}, {"src": "/images/projects/gen-floorplans/Floorplan 9.jpg", "alt": "Capture Quality Improvements"}]
---

At Matterport, getting a floor plan meant submitting a LiDAR capture into a queue, where a human operator manually drew it up. Days of turnaround, no automation in sight. Within my first year at Polycam, we shipped the opposite: a single capture session that automatically generates a 3D model, a 2D floor plan, and a spatial measurement report, all in seconds, with no manual drafting step.

### Problem

iPhone LiDAR is fundamentally less accurate than professional capture hardware, and before Apple's RoomPlan API, Polycam had no reliable way to detect straight wall surfaces, the prerequisite for trustworthy measurement data. AEC professionals needed floor plans they could actually use on the job, and the market only offered expensive and slow (manual services) or cheap and inaccurate. Nothing produced a client-ready asset directly from a phone scan.

### Constraints

Consumer LiDAR has an accuracy ceiling well below professional hardware. Apple's RoomPlan API was a black box, no visibility into its roadmap or future investment. Team size: me and one computer vision engineer to start. That scarcity forced a bias toward shipping early and rough over waiting for polish.

### Move

Ship on RoomPlan first to get something real in customers' hands fast, then iterate based on what they actually used it for. In parallel, invest in our own custom reconstruction so we weren't permanently dependent on Apple's roadmap.

### Outcome

Measurement accuracy reached ±1 to 3 inches, professional grade, with 3D, 2D, and a spatial measurement report generated automatically from a single capture. That capability became a primary driver of Polycam's Pro tier growing from $1.5M to $12M ARR [over 2 years], before any paid floor plan editing existed.

The next bet was on packaging. Usage data showed AEC customers using Room mode capture converted to paid at meaningfully higher rates than the rest of the base. We tested that signal by gating Advanced Floor Plan features behind a new Enterprise tier, confirmed willingness to pay, then opened a self-serve Business tier in mid-2024. Growth was slow at first, 0 to 2,000 customers over the following year as we proved the model. In late 2025 we moved all floor plan functionality behind Business, but the real inflection came in January 2026, when we shipped the 2D/3D editor to all customers as the conversion trigger. That paywall converted at 12%, double our baseline rate. Business tier customers went from 2,000 to nearly 10,000 in the six months that followed, the fastest-growing segment in the company.

The product also reached parity with established players like Matterport and Magic Plan, and drew early acquisition interest from a company evaluating the category.