import java.awt.*;
import java.util.*;
import javax.swing.*;
import java.awt.event.*;
public class Creature 
{
   protected int myX;
   protected int myY;
   protected Image image;
   protected boolean isVisible;
   public Creature(String imageName)
   {
      myX=200;
      myY=200;
      isVisible=true;
      ImageIcon i = new ImageIcon(imageName);
      
      image = i.getImage();
   }
   public int getX()
   {
      return myX;
   }
   public int getY()
   {
      return myY;
   }
   public void setX(int x)
   {
      myX=x;
   }
   public void setY(int y)
   {
      myY=y;
   }
   public boolean getVisible()
   {
      return isVisible;
   }
   
   public void setVisible(boolean b)
   {
      isVisible=b;
   }

   public Image getImage()
   {
      return image;
   }
   public void setImage(Image i)
   {
      image=i;
   }
   public Rectangle getBox()
   {
      return new Rectangle(myX,myY,image.getWidth(null),image.getHeight(null));     //used to see if two entities intersect
   }
}


 

