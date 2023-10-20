/**************************************************************************
* The character is the image that is controlled by the user. He can shoot bullets and has 3 health points.
*@author Steven Li
*@version 5/22/2019
**********************************************************************/



import java.awt.*;
import java.util.*;
import javax.swing.*;
import java.awt.event.*;
public class Character extends Creature
{
   private int dx;
   private int dy;
   private int hp;
   private ArrayList<Bullet> array;
   /************************************************************************
   * Constructs the character with x and y coordinate values, movement
   * values, hit points, and the image specified by imageName
   * @param imageName    character's image
   **************************************************************************/
   public Character(String imageName)
   {
      super(imageName);
      myX=200;
      myY=200;
      dx=0;
      dy=0;
      hp=3;
      array=new ArrayList<Bullet>();
   }
   /**************************************************************************
   *Returns character's hp
   * @return hp
   ***************************************************************************
   public int getHP()
   {
      return hp;
   }
   /**************************************************************************
   * sets character's hp
   * @param h     assigns h to hp
   **************************************************************************/
   public void setHP(int h)
   {
      hp=h;
   }
   /**************************************************************************
   * getters method for dx
   * @return dx
   **************************************************************************/
   public int getdx()
   {
      return dx;
   }
   /**************************************************************************
   * getter method for dy
   * @return dy
   **************************************************************************/
   
   public int getdy()
   {
      return dy;
   }
   /**************************************************************************
   * setter method for dx
   * @param x     assigns x to dx
   **************************************************************************/
   public void setdx(int x)
   {
      dx=x;
   }
   /**************************************************************************
   * setter method for dy
   * @param y     assigns y to dy
   **************************************************************************/
   public void setdy(int y)
   {
      dy=y;
   }
   /**************************************************************************
   * returns the list of bullets
   * @return bullet arraylist
   **************************************************************************/
   
   public ArrayList<Bullet> getBullets()
   {
      return array;
   }
   /**************************************************************************
   * removes a bullet from the array
   * @param b   removes bullet b from array
   **************************************************************************/
   public void remove(Bullet b)
   {
      array.remove(b);
   }
   /**************************************************************************
   * shoots a bullet
   * @param s   sets speed of bullet
   * @param angle sets angle of bullet
   **************************************************************************/
   public void shoot(int s, double angle)
   {
      array.add(new Bullet(myX+15,myY+15,s,angle,"circle6.png",5,5));
   }
   /**************************************************************************
   * moves the character
   *@param s     right side boundary
   *@param b     bottom boundary
   **************************************************************************/
   
   public void move(int s, int b)
   {
        myX=myX+dx;
        myY=myY+dy;

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
   

    
    

    
      
 }