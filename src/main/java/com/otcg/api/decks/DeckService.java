package com.otcg.api.decks;
import com.otcg.api.FileService;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;


@Service
public class DeckService {

    private HashMap<String,DeckModel> decks = new HashMap<String, DeckModel>();
    private FileService fs = new FileService();

    public DeckModel getDeck(String id) {
        //how to return a custom response if decks.get(id) fails??
        DeckModel targetDeck = decks.get(id);
        return targetDeck;

    }

    public String createDeck(DeckModel newDeck) {

        String deckId = newDeck.getId();
        String deckTcg = newDeck.getDeckTcg();
        String deckName = newDeck.getDeckName();
        if (!decks.containsKey(deckId)){
            decks.put(deckId, newDeck);
            fs.uploadDeck(newDeck);
            return String.format("Deck has been created: Deck for %s Name:%s Id:%s", deckTcg, deckName, deckId);
        }
       return String.format ("A deck for %s already exists with Name: %s and Id:%s", deckTcg, deckName, deckId);
    }

    public Boolean updateDeck(DeckModel updatedDeck) {
        try {
            //properties of updated deck
            String updatedTcg = updatedDeck.getDeckTcg();
            ArrayList updatedCards = updatedDeck.getCards();
            String name = updatedDeck.getDeckName();
            String id = updatedDeck.getId();

            DeckModel targetDeck = getDeck(id);
            ArrayList currentCards = targetDeck.getCards();
            String targetTcg = targetDeck.getDeckTcg();
            boolean isSame = areSame(updatedDeck, targetDeck);
            //reject changing a deck to a different tcg or attempting to update a deck to the same deck

            if (!updatedTcg.equals(targetTcg) || isSame){
                return false;
            }
            //update the deck if there are any differences in content
            if (currentCards != updatedCards){
                targetDeck.setDeck(updatedCards);
            }
            if (targetDeck.getDeckName() != name){
                targetDeck.setDeckName(name);
            }
            return true;
        } catch(Exception e) {
            return false;
        }

    }

    private boolean areSame(DeckModel deck1, DeckModel deck2) {
        String deck1Name = deck1.getDeckName();
        String deck1Id = deck1.getId();
        String deck1Tcg = deck1.getDeckTcg();
        ArrayList deck1Cards = deck1.getCards();
        String deck2Name = deck2.getDeckName();
        String deck2Id = deck2.getId();
        String deck2Tcg = deck2.getDeckTcg();
        ArrayList deck2Cards = deck2.getCards();

        if (deck1Name.equals(deck2Name) && deck1Id.equals(deck2Id) && deck1Tcg.equals(deck2Tcg) && deck1Cards.equals(deck2Cards)){
            return true;
        }
        return false;
    }
    public Boolean deleteDeck(String id) {

            if (!decks.containsKey(id)){
                return false;
            }
            decks.remove(id);
        return true;
    }

    public String getCollection(){

        return "collection";
    }
}