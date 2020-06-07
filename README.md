# HelpMate
P2P Smart Resource Distribution
## Inspiration
Inspired by oriental culture and collective living, our team of three came up with the idea that communities can be very strong in times of crisis. This is even more true when governments and institutions do not have the capacity of managing crisis in poor or underdeveloped countries. In such situations, normally resources don't get distributed in a fair way, prices constantly change in a volatile way, it takes a lot of time and effort to get those goods, and sometimes corruption can also block the resources to reach those in need.

We believe in the power of community, and the conviction that helping people can be rewarded in creative ways, sometimes by adding gamification to make it more fun. We believe that crisis such as COVID-19 can get us closer to each other, our neighbours and local communities, and can positively impact the lives of those vulnerable and in need. We believe by creating a socially purpose-based business we can create a better world. 

## What it does
We are kind of a mix of Waze and a Delivery system for primary goods in cities during the crisis.
**HelpMate** is a platform that allows anyone in the city to easily identify (tag) distribution points (such as drug stores or shops) for primarily good (such as medication), their availability, and price while they walk or shop in the city. It also allows users to submit a request for an item and ask for help, get connected to a helpmate who accepts the request, and delivers that item to the person who requested it. 
By Gamification themes and modules we give incentives to users to tag locations, items, and their updated prices. It also makes users keep updating this information so prices and items availability data reflects real-time data.
This flow of actions and features enables a transparent distribution system for all alongside with benefits such as providing a safe channel of delivery not only for the whole community but also for the weak and vulnerable people. 


## How we built it
As the very first **peer to peer community-based delivery system in crisis** our product is built based on the most challenging technologies of the 4th industrial revolution, such as modern artificially intelligent and block-chain based ** decentralized agents**. 
### Block-chain 
Our system is created on a block-chain based community for guaranteeing the security of delivery based transactions and building trust among the peers. The security of the delivery is backed by the structure of the block-chain community which is based on **encrypted hashed chained blocks** . All delivery **smart contracts** are placed in this block-chain. 
Trust is also another added value of block-chain, since our delivery **smart contracts** are placed inside our block-chain.  This Block-chain is defined as decentralized for both online and offline agent systems of users. Meaning that each user is a ** decentralized node**. 
### AI
#### Decentralized Agents: 
The block-chain is not the only decentralized part of our system. Our system also contains a decentralized AI, which is based on one core agent and other multiple agents. The combination of all these agents makes the brain of our artificial intelligence.
This means that not only the core agent is intelligent but also decentralized agents are individually trained to be intelligent and their intelligence is evolving over time, based on core updates from our servers. 
One of the many tasks that the system can perform is to recommend to our users what is the **collective best** for the whole community, making it an inclusive system.
This inclusivity means that the system priorities the collective best rather than the individual benefit. In order to identify what is best for the whole community, the decision is not only made by our core agent but also elicited from feature vectors that are collected from the intelligence in users' systems. 
The mentioned **feature vector** is user's behavior which is gathered by the behavior analysis of a local intelligent agent. This feature vector will be used to recommend the user what is best for the whole community. For example, based on my searches and upvotes as a user, my agent can create a feature vector that shows to which group of users I belong (for example the group who believes that masks can prevent the transmission of the Virus-simply clustering). 
Then the core agent will recommend me where masks are available for me to buy while already filtering high risk options in my search results, so I wouldn't contribute to the worsening of the problem. 
In this case, my actions would also help the whole community as the main priority, while providing the most optimum response to my needs. 
#### Content Understanding: 
While entries in our database are from our users and from different types of people (in a hurry, low level of education, false entries, etc.) there would be potential human errors in the system for users to find what they look for. Since our system is based on community trust, our **intelligent content-understanding-model** tries to make sense of users' inputs, such as title entries, description entries, reviews, etc.  
#### Smart Pricing:
One of the most complex problems in dealing with Peer to Peer marketplace systems is pricing. While the system satisfies the **service provider** (Delivery person), it also needs to satisfy the **service receiver** (The peer who receives the order). To deal with this problem our system uses a **learning-based model** that is constantly trained and fine-tuned. When demand falls, our reinforcement deep learning model gets a negative point for not being able to match the two peers and find a suitable price for each to accept the deal (submit or accept the order). This situation analysis is based on several factors, from weather conditions to public holidays, which will need a deep model.
In conclusion finding the best price model is enabled by giving positive and negative points to reinforce the best price model.
#### Smart Ranking (& smart marketing):
In order to best use the gamification themes, we are aiming to put incentives inside various priorities of our system, meaning that each user's activity is being stored to help us rank them according to best behaviours. 
Our system learns over time with pattern matching which activities and behaviours by users are **more valuable** and gives higher priority. In the beginning, our rewarding/priority maker system is based on a few activities by users such as: **tagging a location as a distribution point, upvoting or downvoting for articles and locations, introducing new members to join the community, delivering an item, and hight review by other users.**

**Rankings** are usually considered as the first indicators of how users of each system are placed inside the various modules of it. Our idea of smart ranking is based on using the **DRL model** to identify the appreciated behaviours and inputs. We have a community based on delivery and peers who are bringing the input data. So the following sets of modules are defined inside DRL model to identify the patterns:
1. Delivery system: Inputs are the number of deliveries per user and the outputs are the number of successful cases resulted from the delivery system 
2. Request system: Inputs are the number of requests registered per user and outputs are the number of successfull orders
3. Review/commenting system: Inputs are reviews that each user is adding for the quality of the delivery based on a set of pre-defined variables. The outputs are the clusters of various personas ranked and clustered to be adaptable with users. (For example a person who appreciates punctuality would be matched with a delivery who has a higher review in delivery time)
4. Tagging system: Inputs are the location data , added by peers to the system so our platform includes enough resources to provide. Outputs in this case are the results of upvoting or downvoting by users, showing the accuracy and efficiency of the tagged data.
The mentioned modules are added inside of a DRL model  to find the patterns, the patterns are aligned with the general KPIs of our system which are:
1. Number of the requests 
2. Number of the general data entry 
3. Succesfull orders delivered 
With the learning model ranking the variables and finding the optimum points, our KPIs should be satisfied. 


## Challenges we ran into
Our main pillars of challenges were: 
1. How to build a system that can be used by vulnerable users or seniors which are not so tech-savvy? (inclusive design) 
2. How to use decentralized AI modules to recommend the most optimized options in a peer to peer context?
3. How to use our system data to detect major crisis incidents and use the decentralized approach to manage the resources in these types of scenarios?
4. How may we train the system to understand the ranking abnormalities efficiently?
5. How to best incentivize the data entry for the users so that they keep on populating it with good and fresh data?
6. How to create a system that does not require a high level of maintenance and intervention, while being able to keep its data sets update and safe? 
7. How to create a system that keeps the prices, items and the relative information updated constantly without an operator but with peer data?

## Accomplishments that we're proud of
In a relatively short time, the group managed to build the platform from scratch, brainstorm multiple concepts, and then at the end finalized an MVP with the selected features. We managed to implement almost all of the features planned in the primitive stage, now we have a fully functional website including most of the logic and the functionalities. 
We also have the functionalities for user profile management included, enabling ordering, tagging, voting in the pilot platform. 
We have successfully managed to define a learning threshold system in which user reviews are analyzed and clustered so that system can sustain itself and evolve based on the data it receives within the course of time. 
We use a Decentralised Artificial Intelligence for making our distribution system smarter and more trustworthy. We use AI in our recommendation system to show only the optimized options.
All the requests are done via **Block-Chain** to ensure security and trust.  We use block-chain to keep a copy of sensitive data on each user's end in order to keep transparency and avoid abusive usage. When there is a crisis, decentralized agents let the central AI know that something is fishy.  Central AI sends different reports to various users based on their priority. Agents manager the needs in crisis with priority management. 
Our App has Hybrid Pricing to provide a dynamic price estimation depending on factors such as urge, traffic or demand. Reinforcement Learning is used at the starts to find the optimum win-win points. Reinforcement Learning finds the moments where users progress to action

## What we learned
We have learned that the decentralized AI can enable community building and collaboration endeavours more effective. Peer data can change and help alleviating the crisis moment both in developing and under developing countries. 

## What's next for HelpMate
As we have already created the platform, and most of the features as part of the MVP. After this we would have campaigns enabling peers to populate the system with data so that we can have stages of training. This would help us understand the possible shortcomings of the modules and the chance to modify them based on the real data. For MVP our main focus was on pharmacies with limited pre-defined items. The next step would be to expand the system to multi items not limited to medications only.
We do not have any payment nor online prescription options at the moment, but this could be a nice to have in the next stages after the data sets are more mature.
Gamification themes are not activated at the moment for the sake of layers of complexity but after the pilot stage, we are planning to add that in the next possible sprints. 
We also want to add a donation system. Having in mind that the peer to peer systems are more empathic in general, we thought it would be a great new channel of enabling donation for causes that are also related to the crisis or unforeseen situations such as pandemics. Donations can be added for covering peer to peer delivery prices or can be transient causes for specific crisis moments, all with the vision of inclusivity and human centred design in mind.


