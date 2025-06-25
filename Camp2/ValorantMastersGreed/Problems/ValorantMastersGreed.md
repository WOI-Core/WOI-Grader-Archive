
# Valorant Masters Bangkok: Temicide's Gambit

Temicide, G2's star duelist, stood on the precipice of Valorant glory at Masters Bangkok. The roar of the crowd was deafening, a tidal wave of hype crashing against the stage as they faced Paper Rex in the grand finals. Each round was a chess match of calculated aggression and strategic retreats. Temicide knew victory hinged not just on raw skill, but on making the right calls, the right trades, at the right moment.

Paper Rex, known for their hyper-aggressive "W-key" style, would relentlessly push every advantage. Temicide realized G2 needed to counter this by strategically deploying their agents, maximizing each agent's strength against Paper Rex's.

The coach revealed a crucial piece of intel: the relative "strength" of each Paper Rex agent in their usual starting positions for the first 'n' rounds. He also had an assessment of G2's agents strengths in corresponding positions. Temicide's task was to maximize the number of rounds G2 could win by strategically assigning G2 agents to counter Paper Rex agents. An agent from G2 can only be assigned to one agent from Paper Rex.

Given the strengths of Paper Rex's agents and G2's agents for the first 'n' rounds, determine the maximum number of rounds G2 can win. G2 wins a round if their agent assigned to that round has a higher strength than the Paper Rex agent in that round.

**Input**

The first line contains an integer *n* (1 ≤ *n* ≤ 100), representing the number of rounds.
The second line contains *n* space-separated integers, representing the strengths of Paper Rex's agents.
The third line contains *n* space-separated integers, representing the strengths of G2's agents.

**Output**

Output a single integer, the maximum number of rounds G2 can win.

**Example**

<table>
  <tr>
    <th>Input</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>
      3<br>
      1 2 3<br>
      4 5 6
    </td>
    <td>3</td>
  </tr>
    <tr>
    <td>
      3<br>
      6 2 1<br>
      4 5 3
    </td>
    <td>2</td>
  </tr>
   <tr>
    <td>
      4<br>
      4 7 2 5<br>
      6 2 8 1
    </td>
    <td>2</td>
  </tr>
</table>

**Constraints**

*   Time Limit: 1000 ms
*   Memory Limit: 256 MB
