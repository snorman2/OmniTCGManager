package com.otcg.decks;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class DeckService {

    private ArrayList<DeckModel> decks = new ArrayList();

    public DeckModel getDeck(int id) {

        DeckModel targetDeck = decks.stream().filter(d -> d.getId() == id).findFirst().get();
        return targetDeck;

    }

    public String createDeck(DeckModel newDeck) {
        decks.add(newDeck);
        return String.format("Deck has been created: Deck for %s Name:%s Id:%s", newDeck.getDeckTcg(), newDeck.getDeckName(), newDeck.getId());
    }
    //needs to figure out how getDeck() can return it's own custom message with an invalid index.
    public Boolean updateDeck(int id, String tcg, String name, ArrayList newCards) {
        DeckModel targetDeck = getDeck(id);
        ArrayList currentCards = targetDeck.getCards();

        if (targetDeck == null || !(targetDeck instanceof DeckModel) || !(targetDeck.getDeckTcg().equals(tcg)))  {
            return false;
        }
        targetDeck.setDeckName(name);
        if (currentCards != newCards){
            targetDeck.setDeck(newCards);
        }
        return true;
    }

    public String deleteDeck(int id) {
        DeckModel selectedDeck;
        try {
            selectedDeck = decks.stream().filter(d -> d.getId() == id).findFirst().get();
        } catch (Exception e) {
            return String.format("Invalid deck Id: %s Message: %s", id, e);
        }
        decks.remove(selectedDeck);
        return "Deck deleted successfully";
    }

    public String getCollection(){

        return "collection";
    }
}