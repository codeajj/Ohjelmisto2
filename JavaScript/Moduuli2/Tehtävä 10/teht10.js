const candidate_amount = +prompt("How many candidates?");

const candidates = []

for (let i = 0; i < candidate_amount; i++) {
  const name = prompt("Candidate " + i + "'s name").trim().toLowerCase();
  candidates.push({name: name, votes: 0});
}

const voter_amount = +prompt("How many voters?");

for (let i = 0; i < voter_amount; i++) {
  const vote = prompt("Who do you vote for?").trim().toLowerCase();
  if (vote === "") continue;
  const candidate = candidates.find(candidate => candidate.name === vote);
  if (candidate) {
    candidate.votes++;
  }
}

candidates.sort((a, b) => b.votes - a.votes);

const winner = candidates[0]
console.log(`The winner is ${winner.name} with ${winner.votes} votes`)

console.log("Results:")
candidates.forEach(candidate => {
  console.log(`${candidate.name}: ${candidate.votes} votes`);
})