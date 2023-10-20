import java.awt.*;
import java.util.*;
import javax.swing.*;

public class Enemy extends Creature
{
   private int hp;
   private ArrayList<Bullet> array;
   private int level;
   
   public Enemy(String imageName)
   {
      super(imageName);
      myX=(int)(Math.random()*Map.SIDE-60);
      myY=(int)(Math.random()*Map.BOTTOM-60);
      hp=3;
      array=new ArrayList<Bullet>();
      level=1;
   }
   public void setLevel(int l)
   {
      level=l;
   }
   public int getLevel()
   {
      return level;
   }
   public int getHP()
   {
      return hp;
   }
   public void setHP(int a)
   {
      hp=a;
   }
   public ArrayList<Bullet> getBullets()
   {
      return array;
   }
   public void shoot()
   {
      
      array.add(new Bullet(myX,myY,level+2,(int)(Math.random()*360),"circle6.png",5,5));
   }
   public void move(int s,int b)
   {
      int ran1=(int)(Math.random()*2);
      int ran2=(int)(Math.random()*2);
      if(ran1==0)
      {
         myX=myX+1;
      }
      else
      {
         myX=myX-1;
      }
      
      if(ran2==0)
      {
         myY=myY+1;
      }
      else
      {
         myY=myY-1;
      }
      if (myX < 1) 
      {
         myX = 1;
     }

     if (myY < 1) 
     {
         myY = 1;
     }
     if(myX>s)
     {
         myX=myX-image.getWidth(null)-30;
     }
     if(myY>b)
     {
         myY=myY-image.getHeight(null)-30;
     }
   }
   public void die()
   {
      image=null;
      myX=0;
      myY=0;
   }
   
}