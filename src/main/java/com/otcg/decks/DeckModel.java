package com.otcg.decks;

import java.util.ArrayList;

public class DeckModel {
    private int id;
    private String deckName;
    private String deckTcg;
    private ArrayList cards = new ArrayList();

    public Object[] getInfo() {
        return new Object[]{id, deckName, deckTcg};
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
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
