class Card {
    constructor(color,suit,value){
        this.color = color;
        this.suit = suit;
        this.value = value;
        
    }

   
}

//console.log(card.color)
function boost(front,rear){
    return front + rear 
}

//let guarding = [card2.value,card3.value]

//console.log(card1.value + card2.value)
function guard(cardVanguard,guards){
    let result =0
    for (let g = 0; g < guards.length; g++){
        result +=g
    }
    return cardVanguard + result
}

//console.log(guard(card1.value,guarding))
const INITHANDSIZE = 5;
class Player{
	
  constructor(ID,deck){
  	this.ID = ID;
    this.deck = deck;
    this.hand = [];
    this.damage = [];
  }
  
  receiveDamage(card){
    this.damage.push(card)
    return this.damage
  }
  calcDamage(){
  	return this.damage.length
  }
  
  shuffle(array) {
  	var m = array.length, t, i;

  	// While there remain elements to shuffle…
  	while (m) {

    	// Pick a remaining element…
    	i = Math.floor(Math.random() * m--);

    	// And swap it with the current element.
    	t = array[m];
    	array[m] = array[i];
    	array[i] = t;
  	}

  return array;
	}
  initHand(){
  	
    for(let i=0; i < INITHANDSIZE; i++){
    	this.hand.push(this.deck.pop());
    }
  	return this.hand;
  }
  
  drawCard(){
  	this.hand.push(this.deck.pop());
    return this.hand
  }
}


function createDeck(){
  var DECKSIZE = 52;
	const suits = '♠︎ ♥︎ ♣︎ ♦︎'.split(' ');
	var value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
  for(i = 0; i <= suits.length-1;i++ ){
  	for(j=0; j <=value.length-1;j++){
    	let color = i % 2 ? 'red' : 'black';
    	card = new Card(color,suits[i],value[j]);
    	deck.push(card);
  	}
	}
  return deck;
}

var deck = [];
var hand = [];


p1 = new Player("henona",createDeck());
p1.shuffle(p1.deck)
console.log(p1.deck.length)
p1.initHand()
console.log(p1.deck.length)
p1.drawCard()
p1.drawCard()

console.log(p1.deck.length)
console.log(p1.hand)
//console.log(p1.damage)




//console.log(deck)

