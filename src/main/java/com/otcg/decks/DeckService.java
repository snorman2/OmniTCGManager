package com.otcg.decks;
import com.otcg.api.ResponseModel;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class DeckService {

    private ArrayList<DeckModel> decks = new ArrayList();

    private ResponseModel myResponse = new ResponseModel();


    public DeckModel getDeck(int id) {
        DeckModel selectedDeck = decks.stream().filter(d -> d.getId() == id).findFirst().get();
        myResponse.setDeckList(selectedDeck);
        return myResponse.getDeckList();
    }

    public String createDeck(DeckModel newDeck) {
        decks.add(newDeck);
        return String.format("Deck has been created: Deck for %s Name:%s Id:%s", newDeck.getDeckTcg(), newDeck.getDeckName(), newDeck.getId());
    }

    public String updateDeck(int id, String tcg, ArrayList newCards) {
        DeckModel deck = getDeck(id);
        ArrayList currentCards = deck.getCards();
        if (deck.getDeckTcg().equals(tcg)) {
            if (currentCards.equals(newCards)) {
                return "Deck is already up to date";
            } else {
                deck.setDeck(newCards);
                return "Deck has been updated successfully";
            }
        } else {
            return "This deck is for another TCG. Please ensure you're using the correct tcg and deck id";
        }
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

    public ArrayList<DeckModel> getCollection(){
        myResponse.setCollection(decks);
        return myResponse.getCollection();
    }
}