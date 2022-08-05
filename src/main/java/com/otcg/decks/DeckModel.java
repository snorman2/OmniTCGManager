package com.otcg.decks;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import java.util.ArrayList;


public class DeckModel {
    @NotNull(message = "Deck id cannot be null")
    private String id;
    @NotEmpty(message = "Deck name cannot be blank")
    private String deckName;
    @NotEmpty(message = "Tcg cannot be blank")
    private String deckTcg;
    @NotEmpty(message = "Deck cannot be empty. Deck must at least contain 1 card.")
    private ArrayList cards = new ArrayList();

    public Object[] getInfo() {
        return new Object[]{id, deckName, deckTcg};
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getDeckName() {
        return deckName;
    }

    public void setDeckName(String deckName) {
        this.deckName = deckName;
    }

    public String getDeckTcg() {
        return deckTcg;
    }

    public void setDeckTcg(String deckTcg) {
        this.deckTcg = deckTcg;
    }

    public ArrayList getCards() {
        return cards;
    }

    public void setDeck(ArrayList cards) {
        this.cards = cards;
    }
}
