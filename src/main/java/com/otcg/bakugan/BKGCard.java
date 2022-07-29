package com.otcg.bakugan;

/**
 * <pre>
 *
 *  OTCG Manager
 *  File: BKGCard.java
 *
 *
 *  Description:
 *  The class enumerate various  types of ETRANSACTION table
 *
 * </pre>
 */

public class BKGCard {

    int number;
    String cardName;
    String cardType;
    String faction;
    int energyCost;
    Object pairedBakuCores;
    String baseBakugan;
    int bPower;
    int damage;
    String rarity;

    public Object[] getInfo() {
        return new Object[]{number, cardName, cardType, faction, energyCost, pairedBakuCores, baseBakugan, bPower, damage, rarity};
    }

    public String getCardName(){
        return cardName;
    }

    public String getCardType(){
        return cardType;
    }

    public int getEnergyCost(){
        return energyCost;
    }

    public Object getPairedBakuCores(){
        return pairedBakuCores;
    }

    public String getBaseBakugan(){
        return baseBakugan;
    }

    public int getbPower(){
        return bPower;
    }

    public int getDamage(){
        return damage;
    }

    public String getRarity(){
        return rarity;
    }

    public void setNumber(int n){
        this.number = n;
    }

    public void setCardName(String name){
        this.cardName = name;
    }

    public void setCardType(String type){
        this.cardType = type;
    }

    public void setFaction(String f){
        this.faction = f;
    }

    public void setEnergyCost(int cost){
        this.energyCost = cost;
    }

    public void setPairedBakuCores(Object cores){
        this.pairedBakuCores = cores;
    }

    public void setBaseBakugan(String base){
        this.baseBakugan = base;
    }

    public void setbPower(int power){
        this.bPower = power;
    }

    public void setDamage(int dmg){
        this.damage = dmg;
    }

    public void setRarity(String r){
        this.rarity = r;
    }
}
