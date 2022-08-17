package com.otcg.tcgs.bakugan;

/**
 * <pre>
 *
 *  OTCG Manager
 *  File: BKGCardModel.java
 *
 *
 *  Description:
 *  Card Model class for Bakugan
 *
 * </pre>
 */

public class BKGCardModel {

    private int number;
    private String cardName;
    private String cardType;
    private String faction;
    private int energyCost;
    private Object pairedBakuCores;
    private String baseBakugan;
    private int bPower;
    private int damage;
    private String rarity;

    public Object[] getInfo() {
        return new Object[]{number, cardName, cardType, faction, energyCost, pairedBakuCores, baseBakugan, bPower, damage, rarity};
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public String getCardName() {
        return cardName;
    }

    public void setCardName(String cardName) {
        this.cardName = cardName;
    }

    public String getCardType() {
        return cardType;
    }

    public void setCardType(String cardType) {
        this.cardType = cardType;
    }

    public String getFaction() {
        return faction;
    }

    public void setFaction(String faction) {
        this.faction = faction;
    }

    public int getEnergyCost() {
        return energyCost;
    }

    public void setEnergyCost(int energyCost) {
        this.energyCost = energyCost;
    }

    public Object getPairedBakuCores() {
        return pairedBakuCores;
    }

    public void setPairedBakuCores(Object pairedBakuCores) {
        this.pairedBakuCores = pairedBakuCores;
    }

    public String getBaseBakugan() {
        return baseBakugan;
    }

    public void setBaseBakugan(String baseBakugan) {
        this.baseBakugan = baseBakugan;
    }

    public int getbPower() {
        return bPower;
    }

    public void setbPower(int bPower) {
        this.bPower = bPower;
    }

    public int getDamage() {
        return damage;
    }

    public void setDamage(int damage) {
        this.damage = damage;
    }

    public String getRarity() {
        return rarity;
    }

    public void setRarity(String rarity) {
        this.rarity = rarity;
    }
}
