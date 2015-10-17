package models;

/**
 * Created by Krishna Ghatia on 10/17/2015.
 */
/*
import android.os.Parcel;
import android.os.Parcelable;

import java.util.ArrayList;

public class Trip implements Parcelable {

    // Member fields should exist here, what else do you need for a trip?
	// Please add additional fields
    private int tripId;
	private String name;
    private String tripDestination;
    private int time;
    //private static int tripId=0;
    ArrayList<Person> attenders=new ArrayList<Person>();
    //private String attenders;

    //Person[] attenders=new Person[numberOfAttenders];

    /**
	 * Parcelable creator. Do not modify this function.
	 */
/*
import android.os.Parcel;
import android.os.Parcelable;

public static final Parcelable.Creator<Trip> CREATOR = new Parcelable.Creator<Trip>() {
public Trip createFromParcel(Parcel p) {
        return new Trip(p);
        }

public Trip[] newArray(int size) {
        return new Trip[size];
        }
        };

public Trip(){
        this.tripId = 0;
        this.name = "";
        this.tripDestination = "";
        this.time = 0;
        this.attenders = null;
        }


**
 * Create a Trip model object from a Parcel. This
 * function is called via the Parcelable creator.
 *
 * @param p The Parcel used to populate the
 * Model fields.
 *
public Trip(Parcel p) {
        tripId = p.readInt();
        name = p.readString();//p.readTypedList(attenders, Person.CREATOR);
        time=p.readInt();
        tripDestination=p.readString();
        attenders=p.readArrayList(null);
        //tripId=p.readInt();


        //creator=p.readString();

        // TODO - fill in here
        }


 * Create a Trip model object from arguments
 *
 * @param name  Add arbitrary number of arguments to
 * instantiate Trip class based on member variables.

public Trip( String name, String tripDestination, int time) {
        this.tripId = tripId;
        this.name=name;
        this.tripDestination=tripDestination;
        this.time=time;
        //this.creator=creator;
        //this.attenders=attenders;
        // TODO - fill in here, please note you must have more arguments here
        }

*
 * Serialize Trip object by using writeToParcel.
 * This function is automatically called by the
 * system when the object is serialized.
 *
 * @param dest Parcel object that gets written on
 * serialization. Use functions to write out the
 * object stored via your member variables.
 *
 * @param flags Additional flags about how the object
 * should be written. May be 0 or PARCELABLE_WRITE_RETURN_VALUE.
 * In our case, you should be just passing 0.
 *

@Override
public void writeToParcel(Parcel dest, int flags) {
        dest.writeInt(tripId);
        dest.writeString(name);
        dest.writeInt(time);
        dest.writeString(tripDestination);
        dest.writeList(attenders);
        // dest.writeString(creator);
        // TODO - fill in here
        }

public ArrayList<Person> getAttenders(){return  attenders;}

public String getName(){
        return name;
        }

public String getTripDestination() {
        return tripDestination;
        }

public void setTripDestination(String tripDestination) {
        this.tripDestination = tripDestination;
        }

public void setName(String name) {
        this.name = name;
        }

public int getTime()
        {
        return time;
        }

public void setTime(int time) {
        this.time = time;
        }

public int getTripId() {
        return tripId;
        }

public void setTripId(int tripId) {
        this.tripId = tripId;
        }

public void setAttenders(Person person){
        attenders.add(person);
        }

    //public void setAttenders(String attenders) {
     //   this.attenders = attenders;
    //}
*
 * Feel free to add additional functions as necessary below.



 * Do not implement

@Override
public int describeContents() {
        // Do not implement!
        return 0;
        }
        }

* */

import android.os.Parcel;
import android.os.Parcelable;

import java.util.ArrayList;

public class User implements Parcelable {

    // Member fields should exist here, what else do you need for a trip?
    // Please add additional fields
    private String userId;
    private String name;
    private String emailId;
    private boolean isVolunteer;
    private String homeAddress;
    private String occupation;

    public static final Parcelable.Creator<User> CREATOR = new Parcelable.Creator<User>() {
        public User createFromParcel(Parcel p) {
            return new User(p);
        }

        @Override
        public User[] newArray(int i) {
            return new User[0];
        }
    };

    public User(){
        this.userId = "";
        this.name = "";
        this.emailId = "";
        this.isVolunteer = false;
        this.homeAddress = "";
        this.occupation = "";
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i) {

    }

    public User(Parcel p) {
        userId = p.readString();
        name = p.readString();//p.readTypedList(attenders, Person.CREATOR);
        emailId = p.readString();
        isVolunteer = p.readByte() != 0;
        occupation = p.readString();

    }

    public User( String userId, String name, String emailId, boolean isVolunteer, String occupation) {
        this.userId = userId;
        this.name = name;
        this.emailId = emailId;
        this.isVolunteer = isVolunteer;
        this.occupation = occupation;
        //this.creator=creator;
        //this.attenders=attenders;
        // TODO - fill in here, please note you must have more arguments here
    }

}
    //private static int tripId=0;
    //ArrayList<Person> attenders=new ArrayList<Person>();
    //private String attenders;

    //Person[] attenders=new Person[numberOfAttenders];