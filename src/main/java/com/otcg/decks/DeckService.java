package com.otcg.decks;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class DeckService {

    private List<DeckModel> decks = new ArrayList();

    public List<DeckModel> getAllDecks(){
        return decks;
    }

    public DeckModel getDeck(int id){
        return decks.stream().filter(d -> d.getId() == id).findFirst().get();
    }

    public String createDeck(int id, String name, String tcg, ArrayList cards){
        DeckModel deck = new DeckModel();
        deck.setId(id);
        deck.setDeckName(name);
        deck.setDeckTcg(tcg);
        deck.setDeck(cards);

        decks.add(deck);

        return String.format("Deck has been created: Deck for %s Name:%s Id:%s", tcg, name, id);
    }

    public String updateDeck(int id, String tcg, ArrayList newCards){
        DeckModel deck = getDeck(id);
        ArrayList currentCards = deck.getCards();
        if (deck.getDeckTcg().equals(tcg)){
            if (currentCards.equals(newCards)){
                return "Deck is already up to date";
            } else {
                deck.setDeck(newCards);
                return "Deck has been updated successfully";
            }
        }
        else {
            return "This deck is for another TCG. Please ensure you're using the correct tcg and deck id";
        }
    }
}
